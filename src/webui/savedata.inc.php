<?php

include "DB.class.php";


class DataSubmitter {

   const DEV_TYPE_DESKTOP = 0;
   const DEV_TYPE_LAPTOP = 1;
   const DEV_TYPE_SERVER = 2;
   const DEV_TYPE_PHONE = 3;

   const DEV_OS_UNKNOWN = -1;
   const DEV_OS_WIN = 0;
   const DEV_OS_LIN = 1;
   const DEV_OS_MAC = 2;

   private $userToken = "";
   private $devTokens = array();


   function DataSubmitter($token=null) {
      //phpinfo();

      $this->db = new DB();

      if (isset($token)) {
         $this->userToken = $token;

         $this->machineDescriptors = $this->get_device_records($token);
      }
   }


   function submit($dataArray) {

/*      foreach($this->db->query("SELECT * FROM test;") as $row){
         print_r($row);
      }*/

      $uid = $this->create_user_record($dataArray);

      $this->userToken = $uid;

      $this->devTokens = $this->create_device_records($dataArray, $uid, false);

      $this->machineDescriptors = $this->get_device_records($uid);

      $this->save_survey_responses($dataArray);
     
   }


   function submitDevices($dataArray) {

      $this->devTokens = $this->create_device_records($dataArray, $this->userToken, true);

      $this->machineDescriptors = $this->get_device_records($this->userToken);

   }


   function getMachineDescriptors() {
      return $this->machineDescriptors;
   } 


   function create_user_record($dataArray) {

      $rn = rand(1, getrandmax());
      $ip = $_SERVER['REMOTE_ADDR'];
      $reqt = $_SERVER['REQUEST_TIME'];

      $user_identifier = substr(sha1($ip.$reqt.$rn), 0, 8);

      $age_id = $_POST["s_p_age"];
      $itcomp_id = $_POST["s_p_itcomp"];
      $occup_id = $_POST["s_p_occup"];
      $dataage_id = $_POST["s_p_dataageguess"];

      $q = $this->db->prepare( "INSERT INTO study_users " .
                        "SET identifier = ?, " . 
                        "signup = ?, " . 
                        "age_id = ?, " .
                        "itcomp_id = ?, " .
                        "occup_id = ?, " .
                        "dataage_id = ?;");

      $res = $q->execute(array($user_identifier, time(), $age_id, $itcomp_id, 
                        $occup_id, $dataage_id));

      return $user_identifier;

   }


   function get_user_token() {
      return $this->userToken;
   }


   function create_device_records($dataArray, $uid, $repost) {

      $hasDesktops = ($_POST['chk_desktops'] == "on");
      $hasLaptops = ($_POST['chk_laptops'] == "on");
      $numDesktops = $_POST['txt_numDesktops'];
      $numLaptops = $_POST['txt_numLaptops'];
      //$numServers = $_POST['txt_numServers'];

      if (!$repost && !($hasDesktops || $hasLaptops)) 
         return false;

      if ($numDesktops < 0 && $numLaptops < 0) 
         return false;

      $q = $this->db->prepare( "INSERT INTO study_devices " .
                        "SET token = ?, " . 
                        "uid = ?, " . 
                        "dev_type = ?, " .
                        "dev_os = ?, " .
                        "data_gathered = ?, " .
                        "time_added = ?, " .
                        "time_data_rx = ?;");

      for ($i = 0; $i < $numDesktops; $i++) {
         $token = substr(sha1($uid.time().$i.self::DEV_TYPE_DESKTOP), 0, 10);
         $devTokens[] = $token;

         $type = self::DEV_TYPE_DESKTOP;
         $os = self::DEV_OS_UNKNOWN;

         $res = $q->execute(array($token, $uid, $type, 
                           $os, 0, time(), 0));
      }

      for ($i = 0; $i < $numLaptops; $i++) {
         $token = substr(sha1($uid.time().$i.self::DEV_TYPE_LAPTOP), 0, 10);
         $devTokens[] = $token;

         $type = self::DEV_TYPE_LAPTOP;
         $os = self::DEV_OS_UNKNOWN;

         $res = $q->execute(array($token, $uid, $type, 
                           $os, 0, time(), 0));
      }

      return $devTokens;
   }


   function get_device_records($uid) {

      $q = $this->db->prepare( "SELECT token, dev_type, dev_os, label FROM study_devices " .
                  "WHERE uid = ?;");

      $res = $q->execute(array($uid));

      $rows = $q->fetchAll();

      $i = 0;
      foreach ($rows as $r) {
         $devs[$i]['token'] = $r['token'];
         $devs[$i]['type'] = $r['dev_type'];
         $devs[$i]['label'] = $r['label'];
         $devs[$i]['os'] = $r['dev_os'];
         $i++;
      }

      return $devs;

   }


   function save_survey_responses($dataArray) {

      //var_dump($_POST);

      $qstring =  "INSERT INTO study_responses " .
                  "SET ";
      
      $i = 0;
      foreach ($_POST as $k => $v) {
         if (strpos($k, 's_p_') !== FALSE) continue;
         if ($i > 0) $qstring .= ", ";
         if (strpos($k, ';') !== FALSE || strpos($v, ';') !== FALSE) continue;
         $qstring .= $k.' = '.$this->convertValue($v);
         $i++;
      }
      $qstring .= ';';

      //echo $qstring;

      $q = $this->db->prepare($qstring);

      $res = $q->execute();

   }


   function convertValue($val) {

      switch ($val) {
         case "off":
         case "None at all":
            return 0;
         case "Very little":
         case "on":
            return 1;
         case "Little":
            return 2;
         case "No indication":
            return 3;
         case "Some":
            return 4;
         case "Reasonably much":
            return 5;
         case "Very much":
            return 6;
         default:
            //echo $val."<br />";
            if(is_numeric($val)) return $val;
            else return -1;
      }

   }

   
   function check_data_uploaded($token) {

      // Code to test if data has been submitted
      $uploaddir = './data';

      $uploadfileexpr = '/^[a-zA-Z0-9\.]+\-'.strtoupper($token).'\-([0-9]+)\.gz$/';
      $files = scandir($uploaddir);

      foreach ($files as $f) {
         if (preg_match($uploadfileexpr, $f, $matches)) {
            return $matches[1];
         }
      }

      return 0;
   }

}



?>

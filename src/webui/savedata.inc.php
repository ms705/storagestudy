<?php


class DB extends PDO
{
   public function __construct($file = 'db_settings.ini') {
      if (!$settings = parse_ini_file($file, TRUE)) throw new Exception('Unable to open ' . $file . '.');

      $dsn = $settings['database']['driver'] . 
               ':host=' . $settings['database']['host'] .
               ((!empty($settings['database']['port'])) ? (';port=' . $settings['database']['port']) : '') .
               ';dbname=' . $settings['database']['dbname'];
      
      parent::__construct($dsn, $settings['database']['username'], $settings['database']['password']);
   }
}

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

         $this->devTokens = $this->get_device_records($token);
      }
   }


   function submit($dataArray) {

/*      foreach($this->db->query("SELECT * FROM test;") as $row){
         print_r($row);
      }*/

      $uid = $this->create_user_record($dataArray);

      $this->userToken = $uid;

      $this->devTokens = $this->create_device_records($dataArray, $uid);

      $this->save_survey_responses($dataArray);
     
   }


   function getDevTokens() {
      return $this->devTokens;
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


   function create_device_records($dataArray, $uid) {

      $hasDesktops = ($_POST['chk_desktops'] == "on");
      $hasLaptops = ($_POST['chk_laptops'] == "on");
      $numDesktops = $_POST['txt_numDesktops'];
      $numLaptops = $_POST['txt_numLaptops'];
      //$numServers = $_POST['txt_numServers'];

      if (!($hasDesktops || $hasLaptops)) 
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

      $q = $this->db->prepare( "SELECT token FROM study_devices " .
                  "WHERE uid = ?;");

      $res = $q->execute(array($uid));

      $rows = $q->fetchAll();

      foreach ($rows as $r) {
         $devTokens[] = $r['token'];
      }

      return $devTokens;

   }


   function save_survey_responses($dataArray) {

      //var_dump($_POST);

   }

}



?>

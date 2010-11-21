<?php

include "DB.class.php";

switch ($_GET['a']) {

   case "sendmail":

      $succ = mail($_GET['address'], "test", "your token: ".$_GET['usertoken']);

      if ($succ) {
         echo "success";
      } else {
         echo "failure";
      }

   break;
   
   case "savelabel":

      $db = new DB();

      if (isset($_GET['token'])) {
         $q = $db->prepare("UPDATE study_devices " .
                           "SET label = ? " . 
                           "WHERE token = ?;");

         $res = $q->execute(array($_GET['label'], $_GET['token']));
      }

      var_dump($db);
      var_dump($q);
      var_dump($res);

   break;

   default:

}

?>

<?php

include "DB.class.php";

switch ($_GET['a']) {

   case "sendmail":

      $address = $_GET['email'];
      $token = $_GET['token'];

      $emailtext = <<<END
Thank you for participating in the Personal Storage Study ran by Malte Schwarzkopf and Dr Steven Hand at the University of Cambridge Computer Laboratory. You have requested your access token to be emailed to this address ($address). Note that we have *not* permanently recorded your email address anywhere, it is not linked to your data, and that there is no log of emails sent accessible to us.

Your access token is:  $token .

You can access the second stage of the study at any time by clicking on the following link:

--> http://www-dyn.cl.cam.ac.uk/~ms705/survey/survey2b.php?token=$token <--

Use this link to access the page on other machines that you want to run the scan client on.

We are very grateful for your participation in this research. If you would like any further information,
please contact Malte Schwarzkopf (malte.schwarzkopf@cl.cam.ac.uk).
END;

      $succ = mail($address, "Your access token for the Cambridge Computer Lab Personal Storage Study", $emailtext, "From: CL Personal Storage Study <ms705@cam.ac.uk>\n");

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

   break;

   case "saveos":

      $db = new DB();

      if (isset($_GET['token'])) {
         $q = $db->prepare("UPDATE study_devices " .
                           "SET dev_os = ? " . 
                           "WHERE token = ?;");

         $res = $q->execute(array($_GET['os'], $_GET['token']));
      }

   break;

   case "wait":

      echo "Please wait for results...";

   break;

   default:

}

?>

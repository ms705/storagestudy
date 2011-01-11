<?php

include "DB.class.php";

$token = $_GET['token'];

switch ($_GET['a']) {

   case "sendmail":

      if (isset($_GET['email']) && $_GET['email'] != '') $address = $_GET['email'];
      else return;

      $emailtext = <<<END
Thank you for participating in the Personal Storage Study ran by Malte Schwarzkopf and Dr Steven Hand at the University of Cambridge Computer Laboratory. You have requested your access token to be emailed to this address ($address). Note that we have *not* permanently recorded your email address anywhere, it is not linked to your data, and that there is no log of emails sent accessible to us.

Your user token is:  $token .

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

      if (isset($token)) {
         $q = $db->prepare("UPDATE study_devices " .
                           "SET dev_os = ? " . 
                           "WHERE token = ?;");

         $res = $q->execute(array($_GET['os'], $_GET['token']));
      }

   break;

   case "check":

      // Code to test if data has been submitted
      $uploaddir = './data';

      $uploadfileexpr = '/^[a-zA-Z0-9\.]+\-'.strtoupper($token).'\-([0-9]+)\.gz$/';
      $files = scandir($uploaddir);

      foreach ($files as $f) {
         if (preg_match($uploadfileexpr, $f, $matches)) {
            echo $matches[1];
            return;
         }
      }

      echo 0;

   break;

   case "wait":
?>
            <div style="text-align: center;"><img style="margin: auto; position: relative;" src="images/hourglass.gif" />
            <p>Waiting for results to be uploaded...</p></div>

            <p style="text-align: center; font-size: 8pt;">Please run the scan client that you downloaded and follow the instructions
            on screen. If the download failed, close this dialog and try again.</p>

            <p style="border: 1px solid orange; background-color: lightyellow; text-align: center;">This machine's token is: <br />
            <span style="font-weight: bold; font-size: 18pt; padding: 3px;"><?php echo strtoupper($token); ?></span><br />
            Please enter this token into the tool when asked for it.</p>

<?php
   break;

   case "waitdone":
?>
            <div style="text-align: center;"><img style="margin: auto; position: relative;" src="images/check.png" />
            <p>Results received. Thank you!</p></div>

            <p style="text-align: center; font-size: 8pt;">
            <a href="" onClick="closeDLDialog('<?php echo strtoupper($token); ?>'); return false;">Close the dialog.</a></p>
<?php
   break;

   default:

}

?>

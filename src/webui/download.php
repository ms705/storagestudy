<?php

$token = $_GET['token'];

$ua = $_SERVER['HTTP_USER_AGENT'];
if (isset($_GET['dev'])) echo $ua."<br /><br />";

if (preg_match("/Linux/i", $ua) > 0) {
   $os = 2;
   $sig .= "Linux ";
} elseif (preg_match("/Windows/i", $ua) > 0) {
   $os = 0;
   $sig .= "Windows ";
} elseif (preg_match("/Macintosh/i", $ua) > 0) {
   $os = 1;
   $sig .= "Mac OS X ";
} else {
   $os = -1;
}

if (preg_match("/i686|368/i", $ua) > 0) {
   $bits = 32;
   $sig .= "(32-bit)";
} elseif (preg_match("/x86_64/i", $ua) > 0) {
   $bits = 64;
   $sig .= "(64-bit)";
} else {
   $bits = -1;
} 

?>

<?php
if (!isset($_GET['sel'])) {
?>
<p>Your operating system was detected as: <b><?php echo $sig; ?></b> (<a href="" onClick="downloadSelectionOptions(<?php echo $os; ?>,'<?php echo$token; ?>'); return false;">incorrect?</a>)</p>

<p>Please use the button below to download the appropriate scanning tool.</p>

<p style="text-align: center;"><input type="submit" id="download-button" onClick="initiateDownload(<?php echo $os; ?>, <?php echo $bits; ?>);" value="Download" /></p>
<?php
} else {
?>
<p>Please download the version of the scanning client appropriate to your operating system below.</p>
<table id="download-table">
   <tr>
      <th>Operating System</th>
      <th>32-bit</th>
      <th>64-bit</th>
   </tr>
   <tr>
      <td><img src="images/icon_windows.gif" style="float: left;" /> Windows</td>
      <td><a href="clients/scanclient-win32.exe" onClick="initiateDownload(0, 32); return false;">Download</a></td>
      <td><a href="clients/scanclient-win64.exe" onClick="initiateDownload(0, 64); return false;">Download</a></td>
   </tr>
   <tr>
      <td><img src="images/icon_macos.gif" style="float: left;" /> Mac OS X</td>
      <td><a href="clients/scanclient-mac32.dmg" onClick="initiateDownload(1, 32); return false;">Download</a></td>
      <td>&ndash;</td>
   </tr>
   <tr>
      <td><img src="images/icon_linux.gif" style="float: left;" /> Linux</td>
      <td><a href="clients/scanclient-lin32.tar.gz" onClick="initiateDownload(2, 32); return false;">Download</a></td>
      <td><a href="clients/scanclient-lin64.tar.gz" onClick="initiateDownload(2, 64); return false;">Download</a></td>
   </tr>
</table>
<?php
}
?>
<p>Please save the executable downloaded and run it.</p>

<p style="border: 1px solid orange; background-color: lightyellow; text-align: center;">This machine's token is: <br />
<span style="font-weight: bold; font-size: 18pt; padding: 3px;"><?php echo strtoupper($token); ?></span><br />
Please enter this token into the tool when asked for it.</p>

<?php
//$browser = get_browser(null, true);
//print_r($browser);
?>


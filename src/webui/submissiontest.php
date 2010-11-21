<?php
/*
 * Created on 30 Jul 2010
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */

echo "Received submission\n";

// Code to test POST submission of data
$uploaddir = './data/';

foreach ($_FILES as $k => $f) {
	$uploadfile = $uploaddir . basename($f['name']).'-'.$k.'-'.time().'.gz';
	
	if (move_uploaded_file($f['tmp_name'], $uploadfile)) {
	    echo "File is valid, and was successfully uploaded.\n";
	} else {
	    echo "Possible file upload attack!\n";
	}
}

?>

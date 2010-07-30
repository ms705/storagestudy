<?php
/*
 * Created on 30 Jul 2010
 *
 * To change the template for this generated file go to
 * Window - Preferences - PHPeclipse - PHP - Code Templates
 */

echo "test";

// Code to test POST submission of data
foreach ($_FILES as $k => $p) {
	echo "received item: " . $k;
} 

echo "\n";

var_dump($_FILES);

?>

<?php

$target_path = "uploads/";
//$filename = uniqid(rand(), true) . '.jpg';
$filename = $_FILES["userfile"]["name"];
$target_path = $target_path . $filename; 

if(copy($_FILES['userfile']['tmp_name'], $target_path)) {
    echo "1";
}
else
{ 
	//echo "0";
	print_r($_FILES);
}
?>

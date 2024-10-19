<?php
require_once "pdo.php";                                                                      //Delete
	session_start();
	

if ( isset($_GET['delete']) ) {
    $sql = "DELETE FROM users WHERE user_id = :user_id";
    //echo "<pre>\n$sql\n</pre>\n";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array(':user_id' => $_SESSION['varname']));
	$_SESSION['delete'] = "Successfully deleted.";
	header("Location:View.php");
	return;
}
if ( isset($_GET['cancel']) ) {
header("Location:View.php");
return;
}

	?>
	<!DOCTYPE html>
<html>
<head>
<title>SEAN MANJALY</title>
</head>
<body>
<form method="GET">
<p>Delete the user  ?
<input type="submit" name="delete" value="Delete"/></p>
<p>
<input type="submit" name="cancel" value="Cancel"/></p>
</form>
</body>
</html>
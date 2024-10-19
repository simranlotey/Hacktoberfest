<?php
require_once "pdo.php";                                                        //View
session_start();
if ( !isset($_SESSION['user_id']) ) {
  die('Not logged in');
}


if (isset($_SESSION['flash'])) {
  echo('<p style="color: green;">'.$_SESSION['flash']."</p>\n");
   unset($_SESSION['flash']);
}
if (isset($_SESSION['delete'])) {
  echo('<p style="color: green;">'.$_SESSION['delete']."</p>\n");
   unset($_SESSION['delete']);
}

if ( isset($_POST['edit'] ) ) 
	{         //Check for login or index
		header("Location: Update.php");
		return;
	}

if ( isset($_POST['logout'] ) ) 
	{         //Check for login or index
		header("Location: Logout.php");
		return;
	}
	
	$stmt = $pdo->query("SELECT user_id,name,email FROM users");
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);

if ( isset($_POST['delete']) ) {
	$_SESSION['varname']=$_POST['user_id'];
		header("Location: Delete.php");
		return;
}

?>



<!DOCTYPE html>
<html>
<head>
<title>SEAN MANJALY</title>
</head>
<body>
	<form method="POST">
	<p>
<input type="submit" name="logout" value="Logout"/></p>
</form>
<table border="1">
<tr>
    <th>User Id</th>
	<th>Name</th>
    <th>Email</th>
  </tr>   
<?php
foreach ( $rows as $row ) {
    echo "<tr><td>";
echo($row['user_id']);
   echo("</td><td>");
    echo($row['name']);
	    echo("</td><td>");
    echo($row['email']);
    echo("</td><td>\n");
	//Modify for action
	echo('<form method="POST"><input type="hidden" ');
    echo('name="user_id" value="'.$row['user_id'].'">'."\n");
    echo('<input type="submit" style="color: red;" name="delete" value="Del">'.'<input type="submit" style="color: green;" name="edit" value="Update">');
    echo("\n</form>\n");
    echo("</td></tr>\n");
}
?>
</table>
<a href="add.php">Add New Entry</a>
</body>
</html>

<?php
	require_once "pdo.php";                                                      //Add
	session_start();
	if (  isset($_SESSION['user_id']) ) 
	{
		die('Not logged in');
	}
	if ( isset($_POST['cancel'] ) ) 
	{         //Check for login or index
		header("Location: view.php");
		return;
	}

	function test_input($data) 
	{
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
	if(isset($_POST['add']))
	{
	
		if(!isset($_POST['name']))
		{
			echo("Name is missing!!!");
	
		}
		
		else if(!isset($_POST['email']))
		{
			echo("Email is missing!!!");
    
		}
		else if( isset($_POST['name']) && isset($_POST['email'])) 
		{
			
				$_SESSION["email"]=$_POST["email"];
				$email = test_input($_SESSION["email"]);
				unset($_SESSION["email"]);
				if (!filter_var($email, FILTER_VALIDATE_EMAIL)) 
				{
					$_SESSION['error'] = "Email must have an at-sign (@)";
					if ( isset($_SESSION['error']) ) 
					{
						echo('<p style="color: red;">'.htmlentities($_SESSION['error'])."</p>\n");
						unset($_SESSION['error']);
					}
  
					//header("Location: login.php");
					return;
				} 
				// return;
   
				else
				{
					//$_POST['user_id']=$_SESSION['user_id'];
					echo("<p>Handling POST data...</p>\n");	
					$sql = "INSERT INTO users (name,email) VALUES (:name, :em)";	
					$stmt = $pdo->prepare($sql);

					$stmt->execute(array(':name' => $_POST['name'],':em' => $_POST['email'])); 
					echo("Record inserted"); 
				}
		}
	}
	
	
	
	/*if ( isset($_POST['delete']) ) 
	{
		$sql = "DELETE FROM autos WHERE auto_id = :zip";
		//echo "<pre>\n$sql\n</pre>\n";
		$stmt = $pdo->prepare($sql);
		$stmt->execute(array(':zip' => $_POST['auto_id']));
	}
*/
?>
<!DOCTYPE html>
<html>
<head>
<title>SEAN MANJALY</title>
</head>
<body>
<p>Add A New Profile</p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
<!--<p>Auto id:
<input type="text" name="auto_id"></p>
-->

<p>Name:
<input type="text" name="name"></p>
<p>Email:
<input type="text" name="email" ></p>
<p>
<input type="submit" name="add" value="Add"></p>
<p>
<input type="submit" name="cancel" value="Cancel"></p>
<!--<p>
<input type="submit" name="view" value="View collection"/></p>-->
</form>

</body>
</html>

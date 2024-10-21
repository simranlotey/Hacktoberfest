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
					return;
				}
				else
				{
					echo("<p>Handling POST data...</p>\n");
					$sql = "INSERT INTO users (name,email,password,userRole) VALUES (:name, :em, :password,:userRole)";
					$stmt = $pdo->prepare($sql);

					$stmt->execute(array(':name' => $_POST['name'],':em' => $_POST['email'],':password' => $_POST['userPassword'],':userRole' => 2));
					$_SESSION['flash'] = "Record inserted";
						$_SESSION['user_id'] = $pdo->lastInsertId();
						$_SESSION['name'] = $row['name'];
						header("Location: usersView.php");
						return;
				}
		}
	}
?>
<!DOCTYPE html>
<html>
<head>
<title>Create Account</title>
</head>
<body>
<p>Create an account</p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
<p>Name:
<input type="text" name="name"></p>
<p>Email:
<input type="text" name="email" ></p>
<p>Passsword:
<input type="password" name="userPassword" ></p>
<p>
<input type="submit" name="cancel" value="Create Account"></p>
</form>
</body>
</html>

<?php
	require_once "pdo.php";                                                 //Login
	session_start();
	function test_input($data)
	{
		$data = trim($data);
		$data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
	}
	if ( isset($_POST['cancel'] ) )
	{
    // Redirect the browser to game.php
		header("Location: index.php");
		return;
	}

	if ( isset($_POST['log'])   )
	{
		if ( isset($_POST['email']) && isset($_POST['pass'])  )
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
		}
		echo("<p>Handling POST data...</p>\n");

		$sql = "SELECT * FROM users
			WHERE email = :em AND password = :pw";


		$_SESSION['password']=$_POST['pass'];
		$_SESSION['email']=$_POST['email'];
		$stmt = $pdo->prepare($sql);
		$stmt->execute(array(
        ':em' => $_POST['email'],                                                   //user_id,name,email,password
        ':pw' => $_POST['pass']));
		$row = $stmt->fetch(PDO::FETCH_ASSOC);


		if ( !($row['password'] == $_POST['pass']) )
		{
			$_SESSION["error"]="Incorrect password";
			if ( isset($_SESSION['error']) )
			{
				echo('<p style="color: red;">'.htmlentities($_SESSION['error'])."</p>\n");
				unset($_SESSION['error']);
			}
		}
		else
		{
			$_SESSION['user_id'] = $row['user_id'];//$row['name'];
			$_SESSION['name'] = $row['name'];
			$_SESSION['flash'] = "Login Success";
			if($row['userRole']==1)
			{
				header("Location: View.php");
				return;
			}
			else {
				header("Location: usersView.php");
				return;
			}


		}
	}/*
if ( isset($_POST['Add'] ) )
	{
    // Redirect the browser to game.php
		header("Location: add.php");
		return;
	}*/
?>
<!DOCTYPE html>
<html>
<head><title>SEAN MANJALY</title></head>
<body>
<p>Please Login</p>
<form method="POST">
<p>Email:
<input type="text" size="40" name="email"></p>
<p>Password:
<input type="password" size="40" name="pass"></p>
<p><input type="submit" name="log" value="Log In"/></p>
<p><input type="button" name="cancel" value="Cancel"></p>
<a href="<?php echo($_SERVER['PHP_SELF']);?>">Refresh</a></p>
</form>

</body>
</html>

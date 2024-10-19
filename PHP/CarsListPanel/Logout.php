<?php // line 1 added to enable color highlight
require_once "pdo.php"; 
session_start();                                                                                      //Logout
unset($_SESSION['name']);
unset($_SESSION['user_id']);
header('Location: index.php');
  ?>
  <!DOCTYPE html>
<html>
<head><title>SEAN MANJALY</title></head>
<body>

<h1>Logging out........</h1>
</body>
</html>
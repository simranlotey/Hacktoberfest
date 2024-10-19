<?php
require_once "pdo.php";
                                                                                                     //Index


$stmt = $pdo->query("SELECT name,email FROM users");
$rows = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html>
<head><title>SEAN MANJALY</title></head>
<body>

<h1>Index</h1>

<a href="Login.php">Please log in</a>



<table border="1">
<?php
foreach ( $rows as $row ) {
    echo "<tr><td>";
    echo("<a href=View.php>".$row['name']."</a>");
    echo("</td><td>");
    echo($row['email']);
    echo("</td>");
    echo("\n</form>\n");
    echo("</tr>\n");
}
?>
</table>
</body>
</html>
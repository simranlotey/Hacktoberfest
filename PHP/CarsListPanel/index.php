<?php
require_once "pdo.php";
                                                                                                     //Index
$stmt = $pdo->query("SELECT * FROM carsCrud");
$rowsOfCar = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html>
<head><title>Car Lounge</title></head>
<body>

<h1>Index</h1>

<h3><a href="Login.php">Please log in</a></h3>
<h3><a href="Add.php">Create account</a> to add cars</h3>


<?php

if(count($rowsOfCar)>0)
{
echo("<table border='1'>
  <thead>
<tr>
<th>Name of the car</th>
<th>Price</th>
<th>Mileage</th>
<th>Image</th>
</tr>
  </thead>
  <tbody>
");
foreach ( $rowsOfCar as $row ) {
  echo "<tr><td>";
  echo("".$row['carName']."");
  echo("</td><td>");
  echo($row['price']);
  echo("</td><td>");
  echo($row['mileage']);
  echo("</td><td>");
  echo("<img src='Images\i1.PNG' />");
  echo("</td>");
  echo("</tr>");
}
echo "</tbody>
</table>";
}
else {
  echo '<h2 style="color:red;">No entry!!!</h2>';
}
 ?>
</body>
</html>

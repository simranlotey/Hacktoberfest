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

if ( isset($_POST['deleteCar'] ) )
	{
    $sql = "DELETE FROM carsCrud WHERE car_Id = :car_Id";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(array(':car_Id' => $_POST['carId']));
		return;
	}

if ( isset($_POST['logout'] ) )
	{         //Check for login or index
		header("Location: Logout.php");
		return;
	}

$stmt = $pdo->query("SELECT * FROM carsCrud WHERE userId=:userId");

  $stmt = $pdo->prepare($sql);
  $stmt->execute(array(
      ':userId' => $_SESSION['user_id']));
  $rowsOfCarByUser = $stmt->fetchAll(PDO::FETCH_ASSOC);


?>



<!DOCTYPE html>
<html>
<head>
<title>View My Cars</title>
</head>
<body>
  <h2>View your cars</h2>
  <?php

  if(count($rowsOfCarByUser)>0)
  {
  echo("<table border='1'>
    <thead>
    <tr>
        <th>Car Id</th>
    	<th>Name</th>
        <th>Price</th>
          <th>Mileage</th>
            <th>Image</th>
              <th>Delete</th>
      </tr>
    </thead>
    <tbody>
  ");

  foreach ( $rowsOfCarByUser as $row ) {
      echo "<tr><td>";
  echo($row['car_Id']);
     echo("</td><td>");
      echo($row['carName']);
  	    echo("</td><td>");
      echo($row['price']);
      echo("</td><td>");
    echo "<img src='.$row['price'].'/>");
    echo("</td><td>");
          echo "<form method='post'><input type='hidden' name='carId' value='".$row['car_Id']."'/>
          <input type='submit' name='deleteCar' value='Delete'/></form>";
      echo("</td></tr>\n");
  }
  echo "</tbody>
  </table>";
  }
else {
  echo("<h3 style='color:red;'>Please add cars!!</h3>");
}
   ?>

</table>
<a href="add.php">Add New Entry</a>
</body>
</html>

<?php
$value=0;
$op1=0;
$op2=0;
$operator=NULL;
$message=NULL;
if(isset($_POST['operate']))
{
  if($_POST['op1']==NULL||$_POST['op2']==NULL)
  {
    $message = "Enter the operands!!";
  }
  else if(!isset($_POST['operator']))
  {
    $message = "Choose the operator";
  }
  else {
    $op1=$_POST['op1'];
    $op2=$_POST['op2'];
    $operator=$_POST['operator'];
    switch  ($operator) {
        case 1:
          $value=$op1+$op2;
          break;
        case 2:
          $value=$op1-$op2;
          break;
        case 3:
          $value=$op1*$op2;
          break;
        case 4:
          $value=$op1/$op2;
          break;
        case 5:
          $value=$op1%$op2;
          break;
        default:
          echo "Choose an operator!!";
          break;
    }
  }
}
if(isset($_POST['clear']))
{
$op1=NULL;
$op2=NULL;
$value=NULL;
  $message = "Memory cleared!!";
}
?>
<!DOCTYPE html>
<html>
<head><title>Simple Calculator</title></head>
<body>

<?php
if(isset($message))
{
  echo "<h3 style='color:green;'>".$message."</h3>";
  unset($message);
}
if(isset($value))
{
  echo "<h3 style='color:green;'>".$value."</h3>";
  unset($value);
}

?>

<form method="post" action="index.php">
<input type="number" name="op1" placeholder="Operand 1" />
<select name="operator" >
<option value="1">+</option>
<option value="2">-</option>
<option value="3">*</option>
<option value="4">/</option>
<option value="5">%</option>
</select>
<input type="number" name="op2" placeholder="Operand 2" />
<input type="submit" name="clear" value="Clear Memory" />
<input type="submit" name="operate" value="Execute" />
</form>
</body>
</html>

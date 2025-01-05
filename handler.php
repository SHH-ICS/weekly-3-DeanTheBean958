<!DOCTYPE html>
<html>

<head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://code.getmdl.io/1.3.0/material.indigo-pink.min.css">
  <script defer src="https://code.getmdl.io/1.3.0/material.min.js"></script>
  <title>Dean's Pizzeria</title>
</head>

<body>

  <?php
  $size = "";
  $toppings = -1;

  # Makes the input the varible "size" and gets the vaules from the input. Also
  # does the same for toppings.
  if (isset($_POST['size'])) {
    $size = $_POST['size'];
  }

  if (isset($_POST['toppings'])) {
    $toppings = $_POST['toppings'];
  }

  # For the input L or XL sets the "sizeCost"
  if ($size == "L") {
    $sizeCost = 6.00;
  } else {
    $sizeCost = 10.00;
  }

  # For the input 0 - 4 toppings sets the "toppingsCost" 
  if ($toppings == 0) {
    $toppingsCost = 0;
  } elseif ($toppings == 1) {
    $toppingsCost = 1;
  } elseif ($toppings == 2) {
    $toppingsCost = 1.75;
  } elseif ($toppings == 3) {
    $toppingsCost = 2.50;
  } else {
    $toppingsCost = 3.35;
  }

  # calaultes the subtotal, tax, and total also makes them have two demical 
  # places
  $sizeCost = number_format($sizeCost, 2);
  $toppingsCost = number_format($toppingsCost, 2);
  $subtotal = number_format($sizeCost + $toppingsCost, 2);
  $tax = number_format($subtotal * 0.13, 2);
  $total = number_format($subtotal + $tax, 2);

  # prints out the size, toppings, subtotal, tax, and total
  echo "<h4>$size pizza: $$sizeCost</h4>\n";
  echo "<h4>$toppings toppings: $$toppingsCost</h4>\n";
  echo "<h4>Your subtotal is: $$subtotal</h4>\n";
  echo "<h4>Your tax is: $$tax</h4>\n";
  echo "<h4>Your total is: $$total</h4>\n";
  ?>

</body>

</html>


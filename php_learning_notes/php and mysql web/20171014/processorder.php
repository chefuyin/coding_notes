<html>
<head>
    <title>BOB'S AUTO PARTS-ORDER RESULTS</title>
    <meta charset="UTF-8">
</head>
<body>
<h1> BOB'S AUTO PARTS</h1>
<h2> ORDER RESULTS</h2>
<?php
//echo "<p>order processed.</p>";
date_default_timezone_set('PRC');
echo "<p>order processed at".date('H:i,jS F Y')."</p>";
$tireqty=$_POST["tireqty"];
$oilqty=$_POST["oilqty"];
$sparkqty=$_POST["sparkqty"];
//echo $tireqty.' tires<br>';
//echo $oilqty.' bottles of oil<br>';
//echo $sparkqty.' spark plugs<br>';

$totalqty =0;
$totalqty=$tireqty+$oilqty+$sparkqty;
if ($totalqty==0){
    echo '<p style="color:red">';
    echo "you did not order anything on the previous page!<br>";
    echo "</p>";
    exit;
}else{
    echo "*********************<br>";
    echo "ITEMS ORDERED: ".$totalqty."<br>";
    $totalamount=0.00;
//define 可以定义常量，前面不需要加$
    define('TIREPRICE',100);
    define('OILPRICE',10);
    define('SPARKPRICE',4);
    $totalamount=$tireqty*TIREPRICE
        +$oilqty*OILPRICE
        +$sparkqty*SPARKPRICE;
    echo "SUBTOTAL: $".number_format($totalamount,2)."<br>";

    $taxrate=0.10;//local sales tax is 10%
    echo "TAX: $".number_format($totalamount*$taxrate,2)."<br>";
    $totalamount=$totalamount*(1+$taxrate);
    echo "TOTAL INCLUDING TAX: $".number_format($totalamount,2)."<br>";

}
$find=$_POST["find"];
//p30 switch
switch ($find){
    case "a":
        echo "<p>REGULAR CUSTOMER.</p>";
        break;
    case "b":
        echo "<p>CUSTOMER REFERRED BY TV ADVERT.</p>";
        break;

    case "b":
        echo "<p>CUSTOMER REFERRED BY PHONE DIRECTORY.</p>";
        break;
    case "b":
        echo "<p>CUSTOMER REFERRED BY WORD OF MOUTH.</p>";
        break;
    default:
        echo "<p>WE DON'T KNOW HOW THIS CUSTOMER FOUND US.</p>";
        break;
}

//p30 ifelse
//if ($find =="a"){
//    echo "<p>REGULAR CUSTOMER.</p>";
//}elseif($find=="b"){
//    echo "<p>CUSTOMER REFERRED BY TV ADVERT.</p>";
//}elseif($find=="c"){
//    echo "<p>CUSTOMER REFERRED BY PHONE DIRECTORY.</p>";
//}elseif($find=="d"){
//    echo "<p>CUSTOMER REFERRED BY WORD OF MOUTH.</p>";
//}else{
//    echo "<p>WE DON'T KNOW HOW THIS CUSTOMER FOUND US.</p>";
//}



//isset测试变量是否存在，empty判断值是否为空
//echo "isset($tireqty):".isset($tireqty)."<br>";
//echo "isset($nothere):".isset($nothere)."<br>";
//echo "empty($tireqty):".empty($tireqty)."<br>";
//echo "empty($nothere):".empty($nothere)."<br>";

//get type
//$a=56;
//echo "<hr>";
//echo gettype($a)."<br>";
//settype($a,'double');
//echo gettype($a)."<br>";
//echo "array: ".is_array($a)."<br>";
//echo "double: ".is_double($a)."<br>";
//echo "int: ".is_int($a)."<br>";
//echo "string: ".is_string($a)."<br>";
//echo "object: ".is_object($a)."<br>";
//echo "null: ".is_null($a)."<br>";
//echo "scalar: ".is_scalar($a)."<br>";
//echo "numeric: ".is_numeric($a)."<br>";
//echo "callable: ".is_callable($a)."<br>";
?>
</body>
</html>

<?php

?>
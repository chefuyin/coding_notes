
<!--/**-->
<!--* Created by PhpStorm.-->
<!--* User: ella-->
<!--* Date: 2017/9/24-->
<!--* Time: 22:24-->
<!--*/-->

<html>
<head>
    <title>
        this is test page
    </title>
    <!--charset解决编码问题-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style>
        .error {color: #FF0000;}
    </style>

</head>
<body>
<?php
echo "today is:".date("Y/M/D"). "<br>";
echo "today is:".date("Y/m/d"). "<br>";
echo "today is:".date("Y.M.D"). "<br>";
echo "today is:".date("Y.m.d"). "<br>";
echo "today is:".date("Y-m-d"). "<br>";
echo "today is:".date("Y-M-D"). "<br>";
echo "today is:".date("l"). "<br>";

?>




<!--多维数组-->
<?php
//$cars=array(
//    array("volvo",22,18),
//    array("bmw",15,13),
//    array("saab",5,2),
//    array("land rover",17,15)
//);
//echo $cars[0][0].": 库存：".$cars[0][1].",销量：".$cars[0][2].".<br>";
//echo $cars[1][0].": 库存：".$cars[1][1].",销量：".$cars[1][2].".<br>";
//echo $cars[2][0].": 库存：".$cars[2][1].",销量：".$cars[2][2].".<br>";
//echo $cars[3][0].": 库存：".$cars[3][1].",销量：".$cars[3][2].".<br>";
//
//for ($row=0;$row<4;$row++){
//    echo "<p><b>ROW NUMBER $row</b></p>";
//    echo "<ul>";
//    for($col =0;$col<3;$col++){
//        echo "<li>".$cars[$row][$col]."</li>";
//    }
//    echo "</ul>";
//}
//?>







</body>
</html>
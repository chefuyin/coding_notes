
<!--/**-->
<!-- * Created by PhpStorm.-->
<!-- * User: ella-->
<!-- * Date: 2017/9/25-->
<!-- * Time: 22:22-->
<!-- */-->

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
<!--即使脚本不存在，include仍会继续运行-->
<h1>welcome to our main page</h1>
<p>text text</p>
<p>text text</p>
<?php
//include 'vars.php';
//echo 'I have a '.$color." ".$car." ."
//?>
<?php
//include 'nofile.php';
//echo 'I have a '.$color." ".$car." ."
//?>
<?php
require 'nofile.php';
echo 'I have a $color $car .';
?>

<!--include 2-->
<!--<div class="menu">-->
<!--    --><?php //include 'menu.php';?>
<!--</div>-->
<!--<h1>welcome to our main page</h1>-->
<!--<p>text text</p>-->
<!--<p>text text</p>-->



<!--include用法-->
<!--<h1>welcome to our main page</h1>-->
<!--<p>text text</p>-->
<!--<p>text text</p>-->
<?php //include 'footer.php';?>



<!--© 2010---><?php //echo date("Y")?>
<?php
//date_default_timezone_set("Asia/Shanghai");//timezone set
//echo "time:".date("h:i:sa");
//echo "<br>";
//$d=mktime(9,12,31,6,10,2015);
//echo "time is:".date("Y-m-d h:i:sa",$d);
//echo "<br>";echo "<br>";
//$e=strtotime("10:38pm April 15 2015");
//echo "time is :".date("Y-m-d h:i:sa",$e);
//echo "<br>";echo "<br>";
//$f=strtotime("tomorrow");
//echo "time is :".date("Y-m-d h:i:sa",$f);
//echo "<br>";echo "<br>";
//$g=strtotime("next Saturday");
//echo "time is :".date("Y-m-d h:i:sa",$g);
//echo "<br>";echo "<br>";
//$h=strtotime("+3 Months");
//echo "time is :".date("Y-m-d h:i:sa",$h);
//?>
<!--print saturday-->
<?php
//$startdate=strtotime("saturday");
//$enddate=strtotime("+6 weeks",$startdate);
//while ($startdate<$enddate){
//    echo date("m-d",$startdate),"<br>";
//    $startdate=strtotime("+1 week",$startdate);
//}
//
//?>
<!--倒计时天数-->
<?php
//echo "<br>";echo "<br>";
//$d1=strtotime("December 31");
//$d2=ceil(($d1-time())/60/60/24);
//echo "still:".$d2."days.";
//?>


</body>
</html>
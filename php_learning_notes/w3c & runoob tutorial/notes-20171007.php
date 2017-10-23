<!--简易发送邮件-->
<?php
//$to="admin@charmlegal.com";
//$subject="test mail";
//$message="hello,this is a test email";
//$from ="chefuyin@foxmail.com";
//$headers="From:$from";
//mail($to,$subject,$message,$headers);
//echo "mail sent";
//?>


<!--session须设置在HTML之前-->
<?php
//session_start();
////$_SESSION["views"]=1;
//if (isset($_SESSION["views"])){
//    $_SESSION["views"]=$_SESSION["views"]+1;
//}else{
//    $_SESSION["views"]=1;
//    echo "views=".$_SESSION["views"];
//}
//?>

<!--cookie要设置在HTML前-->
<?php
//setcookie("user","alex porter",time()+3600)
//
//?>

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

<form action="upload_file.php" method="post" enctype="multipart/form-data">
    <label for="file">filename:</label>
    <input type="file" name="file" id="file">
    <br>
    <input type="submit" name="submit" value="submit">

</form>
<!--验证输入-->
<?php
if (!filter_has_var(INPUT_GET,"email")){
    echo "input type does not exist";
}else{
    if (!filter_input(INPUT_GET,"email",FILTER_VALIDATE_EMAIL)){
        echo "email is not valid";
    }else{
        echo "email is valid";
    }
}
?>

<!--选项和标志用于添加额外过滤选项-->
<?php
//$var =300;
//$int_options=array(
//        "options"=>array(
//            "min_range"=>0,
//            "max_range"=>256,
//        )
//);
//if (!filter_var($var,FILTER_VALIDATE_INT,$int_options)){
//    echo "integer is not valid";
//}else{
//    echo "integer is valid";
//}
//?>


<!--filter_var过滤单一变量-->
<?php
//$int=123;
//if (!filter_var($int,FILTER_VALIDATE_INT)){
//    echo "integer is not valid";
//}else{
//    echo "integer is valid";
//}
//?>



<!--try exception 抓取异常-->
<?php
//function checkNum($number){
//    if ($number>1){
//        throw new Exception("value must be 1 or below");
//    }
//    return true;
//}
//try{
//    checkNum(2);
//    echo "if you see this,the number is 1 or below";
//}catch (Exception $e){
//    echo "message: ".$e->getMessage();
//}
//?>


<!--throw new exception抛出异常-->
<?php
//function checkNum($number){
//    if ($number>1){
//        throw new Exception("value must be 1 or below");
//    }
//    return true;
//}
//checkNum(2)
//?>



<!--trigger_error触发错误-->
<?php
//$test =2;
//if ($test >1){
//    trigger_error("value must be 1 or below");
//}
//?>


<!--set_error_handler自定义处理错误-->
<?php
//function customError($errno,$errstr){
//    echo "<b>Error:</b>[$errno]$errstr";
//}
//set_error_handler("customError");
//
//echo ($test)
//?>



<!--die函数处理错误-->
<?php
//if (!file_exists("w.txt")){
//    die("file not found");
//}else{
//    $file=fopen("w.txt","r");
//}
//?>


<!--打印session-->
<?php
//echo "pageviews=".$_SESSION["views"];
//?>

<!--session_destroy彻底终结session-->
<?php
//session_destroy();
//?>


<!--unset释放session-->
<?php
//unset($_SESSION["views"]);
//?>



<!--删除cookie、打印cookie、判断cookie-->
<?php
//setcookie("user","",time()-3600);
//echo $_COOKIE["user"];
//echo "<br>";
//print_r($_COOKIE);
//echo "<br>";
//if (isset($_COOKIE["user"])){
//    echo "welcome ".$_COOKIE["user"]."<br>";
//}else{
//    echo "welcome guest";
//}
//?>



</body>
</html>
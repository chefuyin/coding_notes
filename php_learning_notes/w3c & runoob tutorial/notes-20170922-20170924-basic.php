
<!DOCTYPE HTML>
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
PHP name e-mail and url verify


<?php
    $nameErr=$emailErr=$genderErr=$websiteErr="";
    $name=$email=$gender=$comment=$website="";
    if($_SERVER["REQUEST_METHOD"]=="POST"){
       if(empty($_POST["name"])){
           $nameErr="name is required";
       }else{
           $name=test_input($_POST["name"]);
           if(!preg_match("/^[a-zA-Z]*$/",$name)){
               //preg_match() 函数检索字符串的模式，如果模式存在则返回 true，否则返回 false。
               $nameErr="only letters and white space allowed";
           }
       }

       if (empty($_POST["email"])){
           $emailErr="email is required";
       }else{
           $email=test_input($_POST["email"]);
           if (!preg_match("/([\w\-]+\@[\w-]+\.[\w-]+)/",$email)){
               $emailErr="Invalid email format";
           }
       }

       if (empty($_POST["website"])){
           $website="";
       }else{
           $website=test_input($_POST["website"]);
           if(!preg_match("/\b(?:(?:https?|ftp):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%
                =~_|]/i",$website)){
               $websiteErr="Invalid URL";
           }
       }

       if (empty($_POST["comment"])){
           $comment="";
       }else{
           $comment=test_input($_POST["comment"]);
       }

       if (empty($_POST["gender"])){
           $genderErr="gender is required";
       }else{
           $gender=test_input($_POST[$gender]);
       }
    }
    function test_input($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
?>
<h2>PHP verify</h2>
<p><span class="error">*必须的字段</span> </p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
    NAME:<input TYPE="text" name="name">
    <span class="error">*<?php echo $nameErr;?></span>

    <br><br>
    EMAIL:<input type="text" name="email">
    <span class="error">*<?php echo $emailErr;?></span>
    <br><br>
    WEBSITE:<input type="text" name="website">
    <span class="error">*<?php echo $websiteErr;?></span>
    <br><br>
    Comment:<textarea name="comment" rows="5" cols="40"></textarea>
    <br><br>
    GENDER:
    <input type="radio" name="gender" value="female">female
    <input type="radio" name="gender" value="male">male
    <span class="error">*<?php echo $genderErr;?></span>
    <br><br>
    <input type="submit" name="submit" value="submit">
</form>

<?php
echo "<h2>您的输入：</h2>";
echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $website;
echo "<br>";
echo $comment;
echo "<br>";
echo $gender;
?>




<!-- 表单必填项验证  --><?php
//   function test_input($data) {
//       $data = trim($data);
//       $data = stripslashes($data);
//       $data = htmlspecialchars($data);
//       return $data;
//   }
//
//   $nameErr=$emailErr=$genderErr=$websiteErr="";
//   $name=$email=$gender=$comment=$website="";
//   if ($_SERVER["REQUEST_METHOD"]=="POST"){
//       if(empty($_POST["name"])){
//           $nameErr="name is required";
//       }else{
//           $name=test_input($_POST["name"]);
//       }
//
//       if (empty($_POST["email"])){
//           $emailErr="email is required";
//       }else{
//           $email=test_input($_POST["email"]);
//       }
//
//       if (empty($_POST["website"])){
//           $websiteErr="WEBSITE is required";
//       }else{
//           $website=test_input($_POST["website"]);
//       }
//
//       if (empty($_POST["comment"])){
//           $comment=" ";
//       }else{
//           $comment=test_input($_POST["comment"]);
//       }
//
//       if (empty($_POST["gender"])){
//           $genderErr="gender is required";
//       }else{
//           $gender=test_input($_POST["gender"]);
//       }
//   }
//   ?>
<!---->
<!--   <form method="post" action="--><?php //echo htmlspecialchars($_SERVER["PHP_SELF"]);?><!--">-->
<!--       NAME:<input TYPE="text" name="name">-->
<!--       <span class="error">*--><?php //echo $nameErr;?><!--</span>-->
<!--       <br><br>-->
<!--       EMAIL:<input type="text" name="email">-->
<!--       <span class="error">*--><?php //echo $emailErr;?><!--</span>-->
<!--       <br><br>-->
<!--       WEBSITE:<input type="text" name="website">-->
<!--       <span class="error">*--><?php //echo $websiteErr;?><!--</span>-->
<!--       <br><br>-->
<!--       <label>Comment:<textarea name="comment" rows="5" cols="40"></textarea> </label>-->
<!--       <br><br>-->
<!--       GENDER:-->
<!--       <input type="radio" name="gender" value="female">female-->
<!--       <input type="radio" name="gender" value="male">male-->
<!--       <span class="error">*--><?php //echo $genderErr;?><!--</span>-->
<!--       <br><br>-->
<!--       <input type="submit" name="submit" value="submit">-->
<!--   </form>-->




<!-- 表单验证  -->
<!--   <form method="post" action="--><?php //echo htmlspecialchars($_SERVER["PHP_SELF"]);?><!--">-->
<!--       NAME:<input type="text" name="name"><br>-->
<!--       EMAIL:<input type="text" name="email"><br>-->
<!--       WEBSITE:<input type="text" name="website"><br>-->
<!--       GENDER:<input type="radio" name="gender" value="female">Female-->
<!--       <input type="radio" name="gender" value="male">Male <br>-->
<!--       Comment:<textarea name="comment" rows="5" cols="40"></textarea><br>-->
<!--       <input type="submit">-->
<!---->
<!--   </form>-->
<!--   --><?php
//   $name=$email=$gender=$comment=$website="";
//
//   if ($_SERVER["REQUEST_METHOD"]=="POST"){
//       $name=test_input($_POST["name"]);
//       $email=test_input($_POST["email"]);
//       $website=test_input($_POST["website"]);
//       $comment=test_input($_POST["comment"]);
//       $gender=test_input($_POST["gender"]);
//       }
//
//       function test_input($data){
//       $data=trim($data);
//       $data=stripcslashes($data);
//       $data=htmlspecialchars($data);
//       return $data;
//       }
//
//   ?>
<!---->
<!--   --><?php
//   echo "你输入的信息是：";
//   echo $name;
//   echo "<br>";
//   echo $email;
//   echo "<br>";
//   echo $website;
//   echo "<br>";
//   echo $comment;
//   echo "<br>";
//   echo $gender;
//
//
//   ?>



<!-- HTTP GET方法获取表单信息  -->
<!--<form action="welcome_get.php" method="get">-->
<!--    name:<input type="text" name="name">-->
<!--    <br>-->
<!--    e-mail:<input type="text" name="email">-->
<!--    <br>-->
<!--    <input type="submit">-->
<!---->
<!--</form>-->


<!-- HTTP POST 方法获取表单信息  -->
<!--<form action="welcome.php" method="post">-->
<!--    name:<input type="text" name="name"><br>-->
<!--    e-mail:<input type="text" name="email"><br>-->
<!--    <input type="submit">-->
<!---->
<!--</form>-->


   <!--$_GET-->
<!--    <a href="/charmlegal/20170922notes.php?subject=PHP&web=W3school.com.cn">测试$GET</a>-->
<!--    --><?php
//    echo "STUDY".$_GET['subject']."at".$_GET['web'];
//    ?>



<!--$_POST收集表单信息-->
<!--   <form method="post" action="--><?php //echo $_SERVER['PHP_SELF'];?><!--">-->
<!--       name:<input type="text" name="fname">-->
<!--       <input type="submit">-->
<!--   </form>-->
<!--   -->
<!--   --><?php
//   $name = $_POST['fname'];
//   echo $name;
//   ?>

<!-- $_REQUEST:收集表单数据  -->
<!--   <form method="post" action="--><?php //echo $_SERVER['PHP_SELF'];?><!--">-->
<!--   NAME:<input type="text" name="fname">-->
<!--       <input type="submit">-->
<!--   </form>-->
<!--   --><?php
//   $name =$_REQUEST['fname'];
//   echo $name;
//   ?>

<!-- $_SERVER：报头、路径、脚本位置信息  --><?php
//   echo $_SERVER['PHP_SELF'];
//   echo "<br>";
//   echo $_SERVER['SERVER_NAME'];echo "<br>";
//   echo $_SERVER['HTTP_HOST'];echo "<br>";
//   echo $_SERVER['HTTP_REFERER'];echo "<br>";
//   echo $_SERVER['HTTP_USER_AGENT'];echo "<br>";
//   echo $_SERVER['SCRIPT_NAME'];echo "<br>";
//   ?>

<!-- $GLOBALS引用全局作用域中可用的全部变量  --><?php
//   $x=75;
//   $y=25;
//
//   function addition(){
//       $GLOBALS['z']=$GLOBALS['x']+$GLOBALS['y'];
//   }
//   addition();
//   echo $z;
//   ?>

<!--arsort:根据值（value）对数组进行降序排序 /krsort:根据键（key）对数组进行降序排序   --><?php
//  $age=array("bill"=>"35","steve"=>"100","peter"=>"26");
//  arsort($age);
//  foreach($age as $x=>$x_value){
//      echo $x.$x_value."<br>";
//  }
//  krsort($age);
//  foreach($age as $y=>$y_value){
//      echo $y.$y_value."<br>";
//  }
//   ?>

<!--asort:根据值（value）对数组进行升序排序 /ksort:根据键（key）对数组进行升序排序   --><?php
//   $age=array("bill"=>"35","steve"=>"100","peter"=>"26");
//   asort($age);
//   foreach($age as $x=>$x_value){
//       echo $x.$x_value."<br>";
//   }
//   ksort($age);
//   foreach($age as $y=>$y_value){
//       echo $y.$y_value."<br>";
//   }
//
//   ?>

<!-- rsort:对数组降序进行排列  --><?php
//   $num =array(3,5,1,22,11);
//   rsort($num);
//   $len=count($num);
//   for($y=0;$y<$len;$y++){
//       echo "the no:".$y." is ".$num[$y]."<br>";
//   }
//   ?>


<!-- sort:对数组进行升序排列  --><?php
//   $car=array("volvo","bmw","saab");
//   sort($car);
//   $length =count($car);
//   for ($x=0;$x<$length;$x++){
//       echo "the no:".$x." is ".$car[$x]."<br>";
//
//   }
//
//   ?>

<!-- 遍历关联数组  --><?php
//   $age =array("bill"=>"35","steve"=>"37","peter"=>"43");
//   foreach ($age as $x=>$x_value){
//       echo "key=".$x.", value=".$x_value;
//       echo "<br>";
//   }
//   ?>

<!--  数组存储多个值 --><?php
//   $car =array("volvo","BMW","SAAB");
//   echo "I like ".$car[0].",".$car[1]." and ".$car[2].".<br>";
//   echo "array car's is ".count($car)."<br>";
//
//   $arrlength =count($car);
//   for ($x=0;$x<$arrlength;$x++){
//       echo $car[$x];
//       echo "<br>";
//   }
//   ?>

<!-- 返回值  --><?php
//   function sum($x,$y){
//       $z=$x+$y;
//       return $z;
//   }
//   echo "85+99=".sum(85,99)."<br>";
//   echo "7+13=".sum(7,13)."<br>";
//   echo "8+99=".sum(8,99)."<br>";
//   ?>

<!-- 默认参数值  --><?php
//   function setHeight($minheight =50){
//       echo "the height is :$minheight<br>";
//   }
//   setHeight(150);
//   setHeight();
//   setHeight(80);
//   ?>

<!--函数参数 --><?php
//   function famlilyName($fname){
//       echo "$fname zhang.<br>";
//   }
//   famlilyName("li");
//   famlilyName("hong");
//   famlilyName("tao");
//   famlilyName("xiao mei");
//   famlilyName("jian");
//   ?>

<!--自定义函数   --><?php
//   function writeMsg(){
//       echo "hello world";
//   }
//   writeMsg();
//   ?>

<!-- foreach循环 类似Python for..in..  --><?php
//   $color = array("red","green","blue","yellow");
//   foreach ($color as $value){
//       echo "$value<br>";
//   }
//   ?>

<!-- for 循环  --><?php
//   for ($x=0;$x<=10;$x++){
//       echo "this number is : $x<br>";
//   }
//   ?>

<!--do...while 先执行再校验  --><?php
//    $x=0;
//
//    do{
//        echo "this num is :$x<br>";
//        $x++;
//    }while($x<=5);
//
//    $y=6;
//    do{
//        echo  "this page is :$y<br>";
//        $y++;
//    }while($y<=5);
//    ?>

<!--  while  --><?php
//    $x=1;
//
//    while ($x<=5){
//        echo "this num is :$x<br>";
//        $x++;
//    }
//    ?>

<!-- switch 语句 --><?php
//    $x=4;
//
//    switch ($x)
//    {
//        case 1:
//            echo "number 1";
//            break;
//        case 2:
//            echo "number 2";
//            break;
//        case 3:
//            echo "number 3";
//            break;
//        default:
//            echo "no number between 1 and 3";
//    }
//
//    ?>

<!-- if...elseif...else语句 --><?php
//    $t=date("H");
//    if ($t<"10"){
//        echo "have a good morning!";
//    }elseif ($t<"20"){
//        echo "have a good day!";
//    }else{
//        echo "have a good night";
//    }
//    ?>

<!-- if...else语句   --><?php
//    $t=date("H");//解决时区报错，在php.ini文件中修改date.timenzone=PRC,并去掉前面的分号
//    if ($t<"20"){
//        echo "have a good day!";
//    }else{
//        echo "have a good night!";
//    }
//    ?>

<!--if语句--><?php
//    $t=date("H");
//    if($t<"20"){
//        echo "have a good day";
//    }
//    ?>

<!-- 数组运算符 --><?php
//    $x=array("a"=>"red","b"=>"green");
//    $y=array("c"=>"blue","d"=>"yellow");
//    $z=$x+$y;
//    var_dump($z);echo "<br>";
//    var_dump($x==$y);echo "<br>";
//    var_dump($x!=$y);echo "<br>";
//    var_dump($x<>$y);echo "<br>";
//    var_dump($x!==$y);echo "<br>";
//    ?>

<!-- 比较运算符   --><?php
//    $x=100;
//    $y="100";
//
//    var_dump($x==$y);
//    echo "<br>";
//    var_dump($x===$y);
//    echo "<br>";
//    var_dump($x!=$y);
//    echo "<br>";
//    var_dump($x!==$y);
//    echo "<br>";
//
//    $a=50;
//    $b=90;
//    var_dump($a>$b);
//    echo "<br>";
//    var_dump($a<$b);
//
//    ?>

<!--递增递减运算符--><?php
//    $x=10;
//    echo ++$x;
//    echo "<br>";
//
//    $y =10;
//    echo $y++;
//    echo "<br>";
//
//    $z=5;
//    echo --$z;
//    echo "<br>";
//
//    $i=5;
//    echo $i--;
//
//
//    ?>

<!-- 字符串串接、串接赋值 --><?php
//    $a='hello';
//    $b=$a." world";
//    echo $b;
//
//    $x="hello";
//    $x.=" world";
//    echo $x;
    ?>

<!-- 赋值运算--><?php
//    $x=10;
//    echo $x;
//    echo "<br>";
//    $y=20;
//    $y+=100;
//    echo $y;
//    echo "<br>";
//    $z=50;
//    $z-=25;
//    echo $z;
//    echo "<br>";
//    $i=5;
//    $i*=6;
//    echo $i;
//    echo "<br>";
//    $j=10;
//    $j/=5;
//    echo $j;
//    echo "<br>";
//    $k=15;
//    $k%=4;
//    echo $k;
//    ?>

<!--四则运算 --><?php
//    $x=10;
//    $y=6;
//    echo ($x+$y);
//    echo "<br>";
//    echo ($x-$y);
//    echo "<br>";
//    echo ($x*$y);
//    echo "<br>";
//    echo ($x/$y);
//    echo "<br>";
//    echo ($x%$y);
//    ?>

<!--定义常量，大小写不敏感--><?php
//    define("GREETING","WELCOME TO W3SCHOOL.COM.CN!",true);//define定义常量，大小写不敏感
//    echo greeting;
//    ?>

<!--定义常量，大小写敏感 --><?php
//    define("greeting","welcome to w3school.com.cn!");//大小写敏感
//    echo greeting;
//    ?>





<!---->
<!--    --><?php
//    echo "hello world";
//
//    ?>


</body>
</html>







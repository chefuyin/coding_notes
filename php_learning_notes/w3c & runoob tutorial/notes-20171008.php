
<!--数据库删除操作-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn =mysqli_connect($servername,$username,$password,$dbname);
//if (mysqli_connect_error()){
//    echo "failed: ".mysqli_connect_error();
//}
//mysqli_query($conn,"DELETE FROM myguests WHERE lastname='moe'");
//mysqli_close($conn);
//?>


<!--update数据库-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn =mysqli_connect($servername,$username,$password,$dbname);
//if (mysqli_connect_error()){
//    echo "failed: ".mysqli_connect_error();
//}
//mysqli_query($conn,"UPDATE myguests SET email='doe@example.com'
//WHERE firstname='John' AND lastname='Doe'");
//mysqli_close($conn)
//
//?>


<!--order by-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn = mysqli_connect($servername,$username,$password,$dbname);
//if (mysqli_connect_error()){
//    echo "failed: ".mysqli_connect_error();
//}
//$result =mysqli_query($conn,"SELECT * FROM myguests ORDER BY reg_date DESC");
//while ($row=mysqli_fetch_array($result)){
//    echo $row['firstname'];
//    echo " ".$row['lastname'];
//    echo " ".$row['email'];
//    echo "<br>";
//}
//mysqli_error($conn);
//?>


<!--WHERE子句-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn = mysqli_connect($servername,$username,$password,$dbname);
//if (!$conn){
//    echo "failed: ".mysqli_connect_error();
//}
//$sql="SELECT * FROM myguests WHERE firstname='john' ";
//$result =mysqli_query($conn,$sql);
//
//while ($row=mysqli_fetch_array($result)){
//    echo $row['firstname']." ".$row["lastname"];
//    echo "<br>";
//}
//mysqli_close($conn);
//?>



<!--面向对象之读取数据-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn = new mysqli($servername,$username,$password,$dbname);
//if ($conn->connect_error){
//    die("failed: ". $conn->connect_error);
//}
//$sql= "SELECT id,firstname,lastname FROM myguests";
//$result=$conn->query($sql);
//if ($result->num_rows>0){
//    while ($row= $result->fetch_assoc()){
//        echo "ID: ".$row["id"]." - NAME: ".$row["firstname"]." ".$row["lastname"]."<br>";
//
//    }
//    }else{
//    echo "0 result";
//}
//$conn->close();
//?>

<!--mysqli预处理语句-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn = new mysqli($servername,$username,$password,$dbname);
//if ($conn->connect_error){
//    die("failed: ". $conn->connect_error);
//}
//$stmt =$conn->prepare("INSERT INTO myguests (firstname,lastname,email) VALUES (?,?,?)");//之前多打了个问号导致错误
//if (!$stmt){
//    echo $stmt->error;
//}
//$stmt->bind_param("sss",$firstname,$lastname,$email);
//
//$firstname="john";
//$lastname="doe";
//$email="john@example.com";
//$stmt->execute();
//
//$firstname="mary";
//$lastname="moe";
//$email="mary@example.com";
//$stmt->execute();
//
//$firstname="julie";
//$lastname="dooley";
//$email="julie@example.com";
//$stmt->execute();
//
//echo "datas insert successfully";
//$stmt->close();
//$conn->close();
//
//?>


<!--面向对象插入多条数据-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn = new mysqli($servername,$username,$password,$dbname);
//if ($conn->connect_error){
//    die("failed: ".$conn->connect_error);
//}
//$sql= "INSERT INTO myguests(firstname,lastname,email)
//VALUES ('mary','moe','mary@example.com');";
//$sql .= "INSERT INTO myguests(firstname,lastname,email)
//VALUES ('julie','dooley','julie@example.com');";
//
//if ($conn->multi_query($sql)===TRUE){
//    echo "insert datas successfully";
//}else{
//    echo "error: ".$sql."<br>".$conn->error;
//}
//$conn->close();
//?>


<!--面向对象插入数据-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn = new mysqli($servername,$username,$password,$dbname);
//if ($conn->connect_error){
//    die("failed: ".$conn->connect_error);
//}
//$sql ="INSERT INTO myguests(firstname,lastname,email)
//VALUES('John','Doe','john@example.com')";
//if ($conn->query($sql)===TRUE){
//    echo "insert data successfully";
//}else{
//    echo "error: ".$sql."<br>".$conn->connect_error;
//}
//$conn->close();

?>


<!--面向对象创建表-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn = new mysqli($servername,$username,$password,$dbname);
//if ($conn->connect_error){
//    die("failed: ".$conn->connect_error);
//}
//$sql="CREATE TABLE myguests(
//id INT (6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
//firstname VARCHAR(30) NOT NULL,
//lastname VARCHAR (30) NOT NULL,
//email VARCHAR (50),
//reg_date TIMESTAMP
//)";
//if ($conn->query($sql)===TRUE){
//    echo "Table myguests created successfully";
//}else{
//    echo "error: ".$conn->connect_error;
//}
//$conn->close();
//?>

<!--面向对象创建数据库-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$conn= new mysqli($servername,$username,$password);
//if ($conn->connect_error){
//    die("conn failed :".$conn->connect_error);
//}
//$sql= "CREATE DATABASE myDB";
//if ($conn->query($sql)===TRUE){
//    echo "database creat successfully";
//}else{
//    echo "error creating database: ".$conn->connect_error;
//}
//$conn->close();
//?>


<!--创建MySQL表-->
<!--面向过程-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$dbname="mydb";
//$conn =mysqli_connect($servername,$username,$password,$dbname);
//if (!$conn){
//    die("failed: ".mysqli_error());
//}
//$sql="CREATE TABLE myguests1(
//id INT (6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
//firstname VARCHAR(30) NOT NULL,
//lastname VARCHAR (30) NOT NULL,
//email VARCHAR (50),
//reg_date TIMESTAMP
//)";
//if (mysqli_query($conn,$sql)){
//    echo "successfully create";
//}else{
//    echo "error: ".mysqli_error($conn);
//}
//?>





<!--创建MySQL数据库-->
<!--PDO-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//try{
//    $conn= new PDO("mysql:host=$servername;dbname=mydb",$username,$password);
//    $conn->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
//    $sql="CREATE DATABASE mydbpdo";
//    $conn->exec($sql);
//    echo "success <br>";
//
//}catch (PDOException $e){
//    echo $sql."<br>".$e->getMessage();
//}
//$conn=null;
//
//?>

<!--面向过程-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$conn =mysqli_connect($servername,$username,$password);
//if (!$conn){
//    die("failed: ".mysqli_connect_error());
//}
//$sql="CREATE DATABASE myDB1";
//if (mysqli_query($conn,$sql)){
//    echo "success";
//}else{
//    echo "error: ".mysqli_error($conn);
//}
//mysqli_close($conn)
//?>






<!--连接MySQL-->
<!--PDO-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//try{
//    $conn=new PDO("mysql:host=$servername;dbname=php_notes",$username,$password);
//    echo "success";
//}catch (PDOException $e){
//    echo $e->getMessage();
//}
//$conn=null;/* 关闭连接*/
//?>

<!--mysqli-面向过程-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$conn =mysqli_connect($servername,$username,$password);
//if (!$conn){
//    die("conn failed: ".mysqli_connect_error());
//
//}
//echo "conn successfully"
//mysqli_close($conn);/* 关闭连接*/
//?>


<!--MySQLi-面向对象-->
<?php
//$servername="localhost";
//$username="root";
//$password="root";
//$conn= new mysqli($servername,$username,$password);
//if ($conn->connect_error){
//    die("fail: ".$conn->connect_error);
//}
//echo "success"
//$conn->close();/* 关闭连接*/
//?>
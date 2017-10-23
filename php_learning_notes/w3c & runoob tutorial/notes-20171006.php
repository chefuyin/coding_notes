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

<!--上传文档-->
<!--<form action="upload_file.php" method="post" enctype="multipart/form-data">-->
<!--    <label for="file">filename:</label>-->
<!--    <input type="file" name="file" id="file">-->
<!--    <br>-->
<!--    <input type="submit" name="submit" value="submit">-->
<!---->
<!--</form>-->


<!--fwrite 写入文档-->
<?php
//$myfile=fopen("testfile.txt","w") or die("error");
//$txt ="bill gates\n";
//fwrite($myfile,$txt);
//$txt="steve jobs\n";
//fwrite($myfile,$txt);
//fclose($myfile);
//?>

<!--fgetc读取单个字符-->
<?php
//$myfile= fopen("dict.txt","r") or die("error");
//while(!feof($myfile)){
//    echo fgetc($myfile)."<br>";
//}
//fclose($myfile);
//?>


<!--feof end of file, 遍历未知长度数据-->
<?php
//$myfile= fopen("dict.txt","r") or die("error");
//while(!feof($myfile)){
//    echo fgets($myfile)."<br>";
//}
//fclose($myfile);
//?>

<!--fget单行读取文件-->
<?php
//$myfile=fopen("dict.txt",'r') or die("error");
//echo fgets($myfile);
//fclose($myfile);
//?>

<!--fread 读取文件-->
<?php
//$myfile=fopen("dict.txt",'r') or die("error");
//echo fread($myfile,filesize("dict.txt"));
//fclose($myfile);
//?>

</body>

</html>



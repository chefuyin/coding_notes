<?php
if ((($_FILES["file"]["type"]=="image/gif")
||($_FILES["file"]["type"]=="image/jpeg")
||($_FILES["file"]["type"]=="image/pjpeg"))
&&($_FILES["file"]["size"]<20000)){
    if ($_FILES["file"]["error"]>0){
        echo "return code: ".$_FILES["file"]["error"]."<br>";
    }else{
        echo "upload: ".$_FILES["file"]["name"]."<br>";
        echo "type: ".$_FILES["file"]["type"]."<br>";
        echo "size: ".($_FILES["file"]["size"]/1024)."KB<br>";
        echo "temp file: ".$_FILES["file"]["tmp_name"]."<br>";
        if (file_exists("upload/".$_FILES["file"]["name"])){
            echo $_FILES["file"]["name"]." already exists.";
        }else{
            move_uploaded_file($_FILES["file"]["name"],"upload/".$_FILES["file"]["name"]);
            echo "stored in :"."upload/".$_FILES["file"]["name"];
        }
    }
}else{
    echo "invalid file";
}

?>


<!--文件上传限制-->
<?php
//if ((($_FILES["file"]["type"]=="image/gif")
//||($_FILES["file"]["type"]=="image/jpeg")
//||($_FILES["file"]["type"]=="image/jpg")
//||($_FILES["file"]["type"]=="image/pjpeg"))
//&&($_FILES["file"]["size"]<2000000)){
//    if ($_FILES["file"]["error"]>0){
//        echo "Error:".$_FILES["file"]["error"];
//    }else{
//        echo "Upload: " . $_FILES["file"]["name"] . "<br>";
//        echo "Type: " . $_FILES["file"]["type"] . "<br>";
//        echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br>";
//        echo "Stored in: " . $_FILES["file"]["tmp_name"];
//    }
//}else{
//    echo "invalid file";
//}
//
//?>



<!--upload文件脚本-->
<?php
//if ($_FILES["file"]["error"]>0){
//    echo "error:".$_FILES["file"]["error"]."<br>";
//}else{
//    echo "upload:".$_FILES["file"]["name"]."<br>";
//    echo "type:".$_FILES["file"]["type"]."<br>";
//    echo "size:".($_FILES["file"]["size"]/1024)."KB"."<br>";
//    echo "stored in :".$_FILES["file"]["tmp_name"]."<br>";
//}
//
//?>
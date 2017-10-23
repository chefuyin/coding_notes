
<?php
$xml= simplexml_load_file("note.xml");

print_r($xml);
echo "<br>";
//输出每个元素
echo $xml->to."<br>";
echo $xml->from."<br>";
echo $xml->heading."<br>";
echo $xml->body."<br>";

//输出每个子节点的元素名称和数据
echo $xml->getName()."<br>";
foreach ($xml->children() as $child){
    echo $child->getName()." : ".$child."<br>";
}
?>



<!--遍历XML-->
<?php
//$xmldoc=new DOMDocument();
//$xmldoc->load("note.xml");
//$x=$xmldoc->documentElement;
//foreach ($x->childNodes AS $item){
//    print $item->nodeName." = ".$item->nodeValue ."<br>";
//}
//?>



<!--加载和输出XML-->
<?php
//$xmldoc= new DOMDocument();
//$xmldoc->load("note.xml");
//print $xmldoc->saveHTML();
//?>


<!--初步测试有误-->
<?php
//$parser=xml_parser_create();
//
//function start($parser,$element_name,$element_attrs){
//    switch ($element_name){
//        case "NOTE":
//            echo "--NOTE --<br>";
//            break;
//        case "To":
//            echo "TO:";
//            break;
//        case "FROM":
//            echo "From:";
//            break;
//        case "HEADING":
//            echo "Heading:";
//            break;
//        case "BODY":
//            echo "Message:";
//    }
//}
//
//function stop($parser,$data){
//    echo $data;
//}
//
//xml_set_element_handler($parser,"start","stop");
//xml_set_character_data_handler($parser,"char");
//$fp=fopen("note.xml","r");
//while($data=fread($fp,4096)){
//    xml_parse($parser,$data,feof($fp)) or die(sprintf("xml error: %s at line %d",xml_error_string(xml_get_error_code($parser)),
//            xml_get_current_line_number($parser)));
//
//}
//xml_parser_free($parser);
//?>
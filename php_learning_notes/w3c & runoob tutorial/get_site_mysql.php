<?php
$q=isset($_GET["q"])?intval($_GET["q"]):'';
if (empty($q)){
    echo 'choose a site';
    exit;
}
$conn= mysqli_connect("localhost","root","root");
if (!$conn){
    die("could not connect:".mysqli_error($conn));
}
mysqli_select_db($conn,'test');
mysqli_set_charset($conn,"utf8");
$sql="SELECT * FROM websites WHERE id ='".$q."'";
$result = mysqli_query($conn,$sql);
echo "<table border ='1'>
<tr>
<th>ID</th>
<th>网站名</th>
<th>网站URL</th>
<th>ALEXA 排名</th>
<th>国家</th>
</tr>";
while ($row =mysqli_fetch_array($result)){
    echo "<tr>";
    echo "<td>".$row["id"]."</td>";
    echo "<td>".$row["name"]."</td>";
    echo "<td>".$row["url"]."</td>";
    echo "<td>".$row["alexa"]."</td>";
    echo "<td>".$row["country"]."</td>";
    echo "</tr>";
}
echo "</table>";
mysqli_close($conn);
?>
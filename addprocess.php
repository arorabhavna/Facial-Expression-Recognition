    <head>
<title>Prakalpa Project</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Karma">
<link class="jsbin" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1/themes/base/jquery-ui.css" rel="stylesheet" type="text/css" />
<script class="jsbin" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
<script class="jsbin" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.0/jquery-ui.min.js"></script>
  <style>
    .padding {
      margin-top: 40px;
      margin-bottom: 20px;
      margin-right: 40px;
      margin-left: 80px;
    }

    body:before {
      content: '';
      position: fixed;
      width: 100vw;
      height: 100vh;
      background-image: url("bg1.jpg");
      background-position: center center;
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-size: cover;
      -webkit-filter: blur(10px);
      -moz-filter: blur(10px);
      -o-filter: blur(10px);
      -ms-filter: blur(10px);
      filter: blur(10px);
      z-index: -1;
    }
            .contact-form
        {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%,-50%);
            width: 400px;
            height: 800px;
            padding: 80px 40px;
            box-sizing: border-box;
            background: rgba(0,0,0,.5);
            color:white;
        }
  </style>
<?php
$target_dir = "temp/";
$target_file = $target_dir . basename($_FILES["fileToUploads"]["name"]);
move_uploaded_file( $_FILES['fileToUploads']['tmp_name'], $target_file );
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if((isset($_POST["person"])!= null) and (isset($_POST["age"])!= null) and (isset($_POST["gender"])!= null) and (isset($_POST["education"])!= null) and (isset($_POST["profession"])!= null)) {
    $check = getimagesize($target_file);
    if($check !== false) {
    $escapedArgumment1 = escapeshellarg($_POST["person"]);
    $escapedArgumment2 = escapeshellarg($target_file);
    $escapedArgumment3 = escapeshellarg($_POST["age"]);
    $escapedArgumment4 = escapeshellarg($_POST["gender"]);
    $escapedArgumment5 = escapeshellarg($_POST["education"]);
    $escapedArgumment6 = escapeshellarg($_POST["profession"]);
    $output=shell_exec("C:\\ProgramData\\Anaconda3\\python.exe C:\\xampp\\htdocs\\prakalpa\\add_imgdb.py $escapedArgumment1 $escapedArgumment2 $escapedArgumment3 $escapedArgumment4 $escapedArgumment5 $escapedArgumment6");
    echo "<div class='contact-form w3-center'><h1>".$output."</h1><br><div>";
    }
 else {
        echo "<div class='contact-form w3-center'><h1>File is not an image or all fields not filled !<h1> <br><div>";

    }
}
?>
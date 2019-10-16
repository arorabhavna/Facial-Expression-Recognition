<!DOCTYPE html>
<html>
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
            height: 500px;
            padding: 80px 40px;
            box-sizing: border-box;
            background: rgba(0,0,0,.5);
            color:white;
        }
  </style>

</head>
<body>

<script>
  function readURL(input) {
    document.getElementById('blah').style.display = 'block';
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $('#blah')
          .attr('src', e.target.result)
          .width(200)
          .height(200);
      };

      reader.readAsDataURL(input.files[0]);
    }
  }
</script>

<!-- Top menu -->
<div class="w3-xlarge w3-center">
  <div class="w3-xlarge w3-center" style="max-width:1200px;margin:auto">
    <div class="w3-center w3-padding-16 w3-center">Facial Analytics</div>
  </div>
</div>
<div class="contact-form">
<form action="process.php" method="post" enctype="multipart/form-data">
     <center>Select image to upload:</center><br><br>
    <div class="w3-center"><input type="file" name="fileToUpload" id="fileToUpload" class="w3-button" onchange="readURL(this);"> 
      <br>
      <br>
     <center><img id="blah" src="#" alt="your image" style="display:none;"></center>
      <br>
      <br>
    <input type="submit" value="Upload Image" name="submit" class="w3-button w3-red w3-center"></div>
</form>
</div>
</div>
</body>
</html>
<?php
$output5=shell_exec("C:\\ProgramData\\Anaconda3\\python.exe C:\\xampp\\htdocs\\prakalpa\\cleanup.py");
?>
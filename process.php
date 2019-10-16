
<?php
$target_dir = "temp/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
move_uploaded_file( $_FILES['fileToUpload']['tmp_name'], $target_file );
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    $check = getimagesize($target_file);
    if($check !== false) {
    $escapedArgumment = escapeshellarg($target_file);
    $output1=shell_exec("C:\\ProgramData\\Anaconda3\\python.exe C:\\xampp\\htdocs\\prakalpa\\recog_extract.py $escapedArgumment");
    $output3=shell_exec("C:\\ProgramData\\Anaconda3\\python.exe C:\\xampp\\htdocs\\prakalpa\\emotion.py");
    $output3=shell_exec("C:\\ProgramData\\Anaconda3\\python.exe C:\\xampp\\htdocs\\prakalpa\\Graph.py");
    header('Location: result.php');
    } else {
        echo "File is not an image.";

    }
}
?>
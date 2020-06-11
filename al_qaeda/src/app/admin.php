
<html>
 <head>
  <title>Al Qaeda</title>
 </head>
 <body>
    <div display = "flex" style ="display: flex; justify-content: space-evenly; border: 5px solid black;">
        <a href="/home.php">Home</a>  <a href="/blog.php">Blog</a>  <a href="/login.php">Member Login</a>
    </div>
   <h1> <center>AdM1n PaGE</center></h1>
    <p>

<?php
session_start(); // start session

// Do authorization check 
if (!isset($_SESSION["user_id"])) {
    header("location: home.php");
    exit; // prevent further execution, should there be more code that follows
}

// After the authorization check, display the flag
echo 'Flag is: flg{filer_flag}'
?>
    </br> <a href="/add_blog.php">Add a blog post, if you like :)</a>
    </p>
 </body>
</html>

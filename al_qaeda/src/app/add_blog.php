

<html>
 <head>
  <title>Al Qaeda</title>
 </head>
 <body>
    <div display = "flex" style ="display: flex; justify-content: space-evenly; border: 5px solid black;">
        <a href="/home.php">Home</a>  <a href="/blog.php">Blog</a>  <a href="/login.php">Member Login</a>
    </div>
   <h1> <center>Add a Post - Verified Members Only</center></h1>
   <div>
   <!-- Basic Login Form -->
   <form method="post" action="" name="signin-form">
    <div class="form-element">
        <label>Title</label>
        <input type="text" name="title" required />
    </div>
    <div class="form-element">
        <label>author</label>
        <input type="text" name="author" required />
    </div>
    <div class="form-element">
        <label>content</label>
        <input type="textbox" name="content" required />
    </div>

    <!-- Submit the login request -->
    <button type="submit" name="add_post" value="add_post">Submit Post</button>
    </form>

<?php
// The login form functionality. 
// The bulk of the login and registration came from this website: https://code.tutsplus.com/tutorials/create-a-php-login-form--cms-33261
include('config.php');
session_start();
 
// Do authorization check 
if (!isset($_SESSION["user_id"])) {
    header("location: home.php");
    exit; // prevent further execution, should there be more code that follows
}

// If a POST request is made to 'login' then the functionality for the login is done. 
if (isset($_POST['add_post'])) {
 
    // Get the username and password from the request variables
    $author = $_POST['author'];
    $title = $_POST['title'];
    $post = $_POST['content']; 
 
    // Make the SQL query to get the username
    $query = $connection->prepare("INSERT INTO blog (title, author, content) VALUES (?,?,?); ");
    $query->execute([$title, $author, $post]);

    // Show the results to the user
    if ($result) {
        echo '<p class="success">Your post did not update!</p>';
    } else {
        echo '<p class="error">Something went wrong!</p>';
    }
}
?>
    </div>
 </body>
</html>

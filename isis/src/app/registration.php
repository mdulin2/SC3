
<html>
 <head>
  <title>Al Qaeda</title>
 </head>
 <body>
    <div display = "flex" style ="display: flex; justify-content: space-evenly; border: 5px solid black;">
        <a href="/home.php">Home</a>  <a href="/blog.php">Blog</a>  <a href="/login.php">Member Login</a>
    </div>
   <h1> <center>Registration - Members Use Only</center></h1>

   <!-- Registration form -->
    <form method="post" action="" name="signup-form">
        <div class="form-element">
            <label>Username</label>
            <input type="text" name="username" pattern="[a-zA-Z0-9]+" required />
        </div>
        <div class="form-element">
            <label>Password</label>
            <input type="password" name="password" required />
        </div>
        <button type="submit" name="register" value="register">Register</button>
    </form>

<?php
// A way to turn off the usage of the page:  --> https://stackoverflow.com/questions/33999475/prevent-direct-url-access-to-php-file/33999539
// Grab database information
include('config.php');
session_start();
 
if (isset($_POST['register'])) {
 
    // Get the username and password from the request variables
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Hash the password 
    $password_hash = md5($password);

    // Creating a new user 
    // Create the safe query for the SQL statement
    $query = $connection->prepare("INSERT INTO users(USERNAME,PASSWORD) VALUES (:username,:password_hash)");
    $query->bindParam("username", $username, PDO::PARAM_STR);
    $query->bindParam("password_hash", $password_hash, PDO::PARAM_STR);
    $result = $query->execute();

    // Show the results to the user
    if ($result) {
        echo '<p class="success">Your registration was successful!</p>';
    } else {
        echo '<p class="error">Something went wrong!</p>';
    }
}
 
?>
    </div>
 </body>
</html>
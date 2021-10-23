

<html>
 <head>
  <title>Al Qaeda</title>
 </head>
 <body>
    <div display = "flex" style ="display: flex; justify-content: space-evenly; border: 5px solid black;">
        <a href="/index.php">Home</a>  <a href="/blog.php">Blog</a>  <a href="/login.php">Member Login</a>
    </div>
   <h1> <center>Login - Verified Members Only</center></h1>
   <div>
   <!-- Basic Login Form -->
   <form method="post" action="" name="signin-form">
    <div class="form-element">
        <label>Username</label>
        <input type="text" name="username" pattern="[a-zA-Z0-9]+" required />
    </div>
    <div class="form-element">
        <label>Password</label>
        <input type="password" name="password" required />
    </div>
    <!-- Submit the login request -->
    <button type="submit" name="login" value="login">Log In</button>
    </form>

<?php
// The login form functionality. 
// The bulk of the login and registration came from this website: https://code.tutsplus.com/tutorials/create-a-php-login-form--cms-33261
include('config.php');
session_start();
 
// If a POST request is made to 'login' then the functionality for the login is done. 
if (isset($_POST['login'])) {
 
    // Get the username and password from the request variables
    $username = $_POST['username'];
    $password = $_POST['password'];
 
    // Make the SQL query to get the username
    $query = $connection->prepare("SELECT * FROM users WHERE USERNAME=:username");
    $query->bindParam("username", $username, PDO::PARAM_STR);
    $query->execute();
    $result = $query->fetch(PDO::FETCH_ASSOC);

    if (!$result) {
        echo md5($password); 
        echo $result['password']; 
        echo '<p class="error">Username password combination is wrong!</p>';
    } else {
        
        if (md5($password) === $result['password']) {

            // Set the value of the session token 
            $_SESSION['user_id'] = $result['id'];
            echo '<p class="success">Congratulations, you are logged in!</p>';
            header("Location: /admin.php");
        } else {
            echo '<p class="error">Username password combination is wrong!</p>';
        }
    }
}
 
?>
    </div>
 </body>
</html>

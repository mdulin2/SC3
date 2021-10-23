


<html>
 <head>
  <title>Al Qaeda</title>
 </head>
 <body>
    <div display = "flex" style ="display: flex; justify-content: space-evenly; border: 5px solid black;">
        <a href="/index.php">Home</a>  <a href="/blog.php">Blog</a>  <a href="/login.php">Member Login</a>
    </div>
   <h1> <center>Blog - Learning the Truth</center></h1>

<?php 

include('config.php');
session_start();

// Displays a single post
function display_blog_post($id, $title, $author, $content, $partial){
    echo '<h2>' . $title . '</h2>'; 
    echo '<p>Written by: <i>' . $author . '</i></p>'; 

    // Partial view of the post
    if($partial === true){
        echo 'Click <a href="/blog.php?id=' . $id . '">here</a> to see full details.'; 
    }

    // See the entire post
    else{ 
        echo $content;         
    }
}

// Create the query
$id = $_GET["id"]; 
if ($id){
    $query = "select id, title, author, content FROM blog WHERE id = " . $id . " ORDER BY id DESC;";
    $partial = false; 
}
else {
    $query = "select id, title, author, content FROM blog ORDER BY id DESC LIMIT 1, 3;";
    $partial = true; 
}



// Get the data for the blog post
$result = $connection->query($query);

// Check & display error from the query
if (!$result) {
    echo "\nPDO::errorInfo():\n";
    print_r($connection->errorInfo());
}

$result->setFetchMode(PDO::FETCH_ASSOC);


// SQL returned as expected
if($result){
    // Display each blog post
    $count = 0; 
    while ($row = $result->fetch()){

        display_blog_post($row['id'], $row['title'], $row['author'], $row['content'], $partial); 
        $count = $count + 1; 
    }

    // If no posts were found for the particular ID
    if($count == 0){
        echo 'The blog post with the id of ' . $id . ' does not exist.'; 
    }
}
else {
     echo $connection->errorInfo();
}


?>
    </div>
 </body>
</html>

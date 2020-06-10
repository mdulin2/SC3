# Solution 

## TLDR; 
- SQLi on id for blog post 
- Dumps creds (md5 hash) 
- Crack one of the hashes to login 
- Flag 

## Thorough View 
- There are four pages (three visible to the viewer): 
    - home
    - blog
    - login 
    - admin (hidden) 
- The blog post also has a subview in order to look at an individual blog post.   
- The website has SQL in order to store credentials and blog posts 
- The creds are in the *users* table and the blog posts are in the *blog* table. 

### SQLi
This view has the following URL: http://something.com/blog.php?id=#  
The query looks like the following: 
``` 
$query = "select id, title, author, content FROM blog WHERE id = " . $id . " ORDER BY id DESC;"; 
```
SQL is a query language that allows for data to be pulled from a database. 
Because the id parameter is just being concatented with the rest of the string, this is vulnerable to **SQL Injection**.  
What does this actually do? Let's view the query: 
- `select id, title, author, content FROM blog WHERE id = #  ORDER BY id DESC;";`
- All this query really does is pull all content from the database where the *id* matches a specific value. 
  
SQLi: 
- The query itself can be **altered** by editing adding additional content to the id parameter. 
- For instance, let's use an *id* of `1 OR 1=1`.
    - `select id, title, author, content FROM blog WHERE id = 1 OR 1=1  ORDER BY id DESC;";`
- Look at that; we've altered the query itself! That's pretty sick! But what can we do with that? 

### UNION Operator 
The main goal of the challenge is to get into the admin panel.  
If we have the ability to siphon arbitrary data out of the database (because we control the query) we can steal data from the *users* table.   
How is this done?: 
- We cannot go back from the original query. So, we want to ADD content to the current query. 
    - A way to continue a query is with the *UNION* (https://www.w3schools.com/sql/sql_union.asp) clause. 
- Now, let's create a query that uses a UNION. 
- For example, let's get the following data: 1,1,1,1: 
    - The *id* of `1 UNION select 1,1,1,1; -- `
    - This translates to the following query: 
        - select id, title, author, content FROM blog WHERE id = 1 UNION select 1,1,1,1; -- ORDER BY id DESC;";`
    - This returns the data 1,1,1,1 (via the select clause ). Then, the `--` is a comment, cancelling the rest of the query. 
    - Why just four 1's: 
        - The query returns FOUR fields. 
        - A UNION operator has to have the same number of fields to return in both the queries. 

### Data Exfiltration 
From the section above, we now know how to run multiple queries. So, let's take out the data!  
The table (with the user information) has the following fields: 
- id 
- username 
- password (which is an md5 hash) 

A NORMAL query to get this would look like the following: 
- `select id, username, password FROM users`.

To get this to work properly (with the right number of return statements), we'll need to use an extra value in the *select* clause. 
- `select 1, id, username, password FROM users`

**NOTE**: 
- The FIRST item (in the query) is NOT used because it is an ID (in the actual PHP code that displays the data). 
- So, notice that the username, password are at the end in order to get the data to display properly.  

Now, wrapping this all together, we have the following id value: 
- `3 UNION select 1, username, password,1 FROM users; --`

This results in the following query that returns all data from the users table: 
```
select id, title, author, content FROM blog WHERE id = 3 UNION select 1, username, password,1 FROM users; -- ORDER BY id DESC;
```

### Getting the Password 
Well crap... these aren't passwords! They are hashed passwords.  
Hashing is used so that (in the event of a data breach) username and passwords cannot instantly be used. For more on hash functions, visit https://en.wikipedia.org/wiki/Hash_function....  
These are just md5 hashs. Put one of the hashes into a site like https://crackstation.net/ will get the password very quickly (md5 is a very weak hashing algorithm).  

Just in case though: 
- admin: almostthere 
- hashing: hashing

### Flag! 
Now, go to login page and use the username and password to login! :)   
Your flag will be waiting for you on the admin panel!

    




// PORT=3001 node bin/www
// each file is its own route!
var express = require("express");
var router = express.Router();
var mysql = require("mysql");
var pbkdf2 = require('pbkdf2');

// Wrapper for MySQL
class Database {
  constructor(config) {
    this.connection = mysql.createConnection({
      host: "localhost",
      user: "root",
      password: "Airjordan23",
      database: "injection"
    });
  }
  query(sql, args) {
    return new Promise((resolve, reject) => {
      this.connection.query(sql, args, (err, rows) => {
        if (err) return reject(err);
        resolve(rows);
      });
    });
  }
  close() {
    return new Promise((resolve, reject) => {
      this.connection.end(err => {
        if (err) return reject(err);
        resolve();
      });
    });
  }
}

async function registerUser(username, password, is_admin){
  var database = new Database();

  // The MySQL.escape is used to prevent SQL Injections
  const queryCheck =
    "SELECT * FROM Login WHERE username = " + mysql.escape(username) + "";
  const hash = pbkdf2.pbkdf2Sync(password, 'NoRainbowTableAttacks!', 1, 32, 'sha512').toString('base64');
  const insertUser =
    "INSERT INTO Login(username,password, is_admin) VALUES(" +
    mysql.escape(username) +
    "," +
    mysql.escape(hash) +
    "," +
    mysql.escape(is_admin) + 
    ");";

  console.log(insertUser);

  // Disallow duplicate usernames
  var rows = await database.query(queryCheck);
  if (rows.length !== 0) {
    database.close();
    return false;
  }

  //insert the user
  var rows = await database.query(insertUser);
  database.close();
  return true;
}

// Register for the user.
async function register(username, password, is_admin){
  const query_info = await registerUser(username, password, is_admin);
  if (query_info === false) {
    return "Duplicate username. Choose a different one.";
  } else {
    return "Success!";
  }
}

/* GET users listing. */
router.post("/", async function(req, res, next) {

  const username = req.body.username;
  const password = req.body.password;
  const is_admin = req.body.is_admin; // Frontend initializes this to FALSE
  console.log(is_admin); 
  const registerResponse = await register(username, password, is_admin);
  res.send(registerResponse);
});

module.exports = router;

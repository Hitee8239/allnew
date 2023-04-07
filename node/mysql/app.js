const express = require('express');
const mysql = require('mysql');
const env = require('dotenv').config({ path: "../../.env" });

const connection = mysql.createConnection({
    host: process.env.host,
    user: process.env.user,
    port: process.env.port,
    password: process.env.password,
    database: process.env.database})

const app = express();



connection.connect(err => {
    if (!err) {
        console.log("Database is connected.....\n\n");
    } else {
        console.log("Error Connecting Database....\n\n");
    }
});

app.get('/', (req, res) => {
    connection.query('select * from st_info', (err, rows, fields) => {
        connection.end();
        if (!err) {
            res.send(rows);
            console.log('The solution is : ', rows);
        } else {
            console.log('Error while performing Query');
        }
    })
})

app.listen(8000, () => {
    console.log('8000 Port : Server Started...');
});
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });
const axios = require('axios');

var connection = new mysql({
    host: process.env.host,
    user: process.env.user,
    password: process.env.password,
    database: process.env.database
});



const app = express()

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

function template_nodata(res) {
    res.writeHead(200);
    var template = `
    <!doctype html>
    <html>
    <head>
        <title>Result</title>
        <meta charset="utf-8">
        <link rel="stylesheet" href="./css/navbar.css">
        <link rel="stylesheet" href="./css/footer.css">
        <link rel="stylesheet" href="./css/main.css">
        <link rel="stylesheet" href="./css/normalize.css">
    </head>
    <body>
        <script src="./components/navbar.js"></script>
        <div class="content">
            <h3>데이터가 존재하지 않습니다.</h3>

        </div>
        <script src="./components/footer.js"></script>
    </body>
    </html>
    `;
    res.end(template);
}

function template_result(result, res) {
    // res.writeHead(200);
    res.send(result);
    return
    // var template = `
    // <!doctype html>
    // <html>
    // <head>
    //     <title>Result</title>
    //     <meta charset="utf-8">
    //     <link rel="stylesheet" href="./css/navbar.css">
    //     <link rel="stylesheet" href="./css/footer.css">
    //     <link rel="stylesheet" href="./css/main.css">
    //     <link rel="stylesheet" href="./css/normalize.css">
    // </head>
    // <body>
    // <script src="./components/navbar.js"></script>
    // <div class="content">
    // <table border="1" style="margin:auto;">
    // <thead>
    //     <tr>
    //     <th>BK_ID</th>
    //     <th>BK_NAME</th>
    //     <th>BK_Writer</th>
    //     <th>BK_Publisher</th>
    //     <th>BK_Status</th>
    //     <th>BK_Grade</th>
    //     <th>BK_detail</th>
    //     </tr>
    // </thead>
    // <tbody>
    // `;
    // for (var i = 0; i < result.length; i++) {
    //     template += `
    // <tr>
    //     <td>${result[i]['BK_ID']}</td>
    //     <td>${result[i]['BK_NAME']}</td>
    //     <td>${result[i]['BK_Writer']}</td>
    //     <td>${result[i]['BK_Publisher']}</td>
    //     <td>${result[i]['BK_Registdate']}</td>
    //     <td>${result[i]['BK_Status']}</td>
    //     <td>${result[i]['BK_Grade']}</td>
    //     <td>${result[i]['BK_detail']}</td>
    // </tr>
    // `;
    // }
    // template += `
    // </tbody>
    // </table>
    // </div>
    // <script src="./components/footer.js"></script>
    // </body>
    // </html>
    // `;
    // res.end(JSON.stringify(template));
}

app.get('/', (req, res) => {
    res.redirect('main.html')
})


// request O, query X
app.get('/book/selectdata', (req, res) => {
    const result = connection.query('select * from bookTbl');
    console.log(result);
    res.send(result);
})

// request O, query X
app.post('/book/selectdata', (req, res) => {
    const result = connection.query('select * from bookTbl');
    console.log(result);
    res.send(result);
})

app.get('/search', (req, res) => {
    const keyword = req.query.q;
    const searchResult = connection.query(`SELECT * FROM bookTbl WHERE BK_NAME LIKE '%${keyword}%' OR BK_Writer LIKE '%${keyword}%'`);
    console.log(searchResult)
    res.send(searchResult)
});




//친구 ip
// axios
//     .get('http://192.168.1.77:8000/select')
//     .then(res => {
//         console.log(`statusCode : ${res.status}`)
//         console.log(res)
//     })
//     .catch(error => {
//         console.log(error)
//     })


// request O, query O
// app.post('/insert', (req, res) => {
//     const { id, pw } = req.body;

//     if (id == "" || pw == "") {
//         // res.send('User-id와 Password를 입력하세요.')
//         res.write(`<script>alert("User-Id와 password를 입력하세요.");</script>`)
//     } else {
//         let result = connection.query("select * from user where userid=?", [id]);
//         if (result.length > 0) {
//             res.writeHead(200);
//             var template = `
//         <!doctype html>
//         <html>
//         <head>
//             <title>Error</title>
//             <meta charset="utf-8">
//         </head>
//         <body>
//             <div>
//                 <h3 style="margin-left: 30px">Registrer Failed</h3>
//                 <h4 style="margin-left: 30px">이미 존재하는 아이디입니다.</h4>
//             </div>
//         </body>
//         </html>
//         `;
//             res.end(template);
//         } else {
//             function confirm(){
//                 window.confirm("컨펌")
//             }
//             if (confirm) {
//                 result = connection.query("insert into user values (?, ?)", [id, pw]);
//                 console.log(result);
//                 res.redirect('/selectQuery?id=' + req.body.id);
//                 alert("입력 완료 .");
//             } else {
//                 alert("취소되었습니다.");
//             }
//         }
//     }
// })

// request O, query O
// app.post('/update', (req, res) => {
//     const { id, pw } = req.body;
//     if (id == "" || pw == "") {
//         // res.send('User-id와 Password를 입력하세요.')
//         res.write(`<script>alert("User-Id , passwd를 입력하세요.");</script>`)
//     } else {
//         const result = connection.query("select * from user where userid=?", [id]);
//         console.log(result);
//         // res.send(result);
//         if (result.length == 0) {
//             template_nodata(res)
//         } else {
//             const result = connection.query("update user set passwd=? where userid=?", [pw, id]);
//             console.log(result);
//             res.redirect('/selectQuery?id=' + id);
//         }
//     }
// })


// request O, query O
// app.post('/delete', (req, res) => {
//     const id = req.body.id;
//     if (id == "") {
//         // res.send('User-id를 입력하세요.')
//         res.write(`<script>alert("User-Id , passwd를 입력하세요.");</script>`)
//     } else {
//         const result = connection.query("select * from user where userid=?", [id]);
//         console.log(result);
//         // res.send(result);
//         if (result.length == 0) {
//             template_nodata(res)
//         } else {
//             const result = connection.query("delete from user where userid=?", [id]);
//             console.log(result);
//             res.redirect('/select');
//         }
//     }
// })

module.exports = app;

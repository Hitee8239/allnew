const oracledb = require('oracledb');
const dbConfig = require('./dbConfig');
const express = require('express');
const path = require('path');

const app = express();

app.set('port', process.env.PORT || 3000);

const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

oracledb.autoCommit = true;

app.get('/', (req,res)=> {
    res.send('Web Server Started~!');
});

app.get('/dbTestSelect',(req, res)=> {
    oracledb.getConnection({
        user: dbConfig.user,
        password: dbConfig.password,
        connectString: dbConfig.connectString
    },
        (err, connection)=> {
            if (err) {
                console.error(err.message);
                return;
            }
            let query = 'select * from usertbl';

            connection.execute(query, [],  (err, result)=> {
                if (err) {
                    console.error(err.message);
                    doRelease(connection);
                    return;
                }
                console.log(result.rows);
                doRelease(connection, result.rows);
            });
        });

    function doRelease(connection, rowList) {
        connection.release(function (err) {
            if (err) {
                console.error(err.message);
            }
            console.log('list size : ' + rowList.length);
            res.send(rowList);
        })
    }
})

app.post('/dbTestInsert',(req, res)=> {
    oracledb.getConnection({
        user: dbConfig.user,
        password: dbConfig.password,
        connectString: dbConfig.connectString
    },
        (err, connection)=> {
            if (err) {
                console.error(err.message);
                return;
            }
            let query = 'insert into usertbl(userid, username , birthyear, addr , mobile1, mobile2, height, mdate)'
                + 'values(:userid, :username , :birthyear, :addr , :mobile1, :mobile2, :height, :mdate)';

            let binddata = [
                req.body.userid,
                req.body.username,
                Number(req.body.birthyear),
                req.body.addr,
                req.body.mobile1,
                req.body.mobile2,
                Number(req.body.height),
                req.body.mdate
            ];

            connection.execute(query, binddata,  (err, result)=> {
                if (err) {
                    console.error(err.message);
                    doRelease(connection);
                    return;
                }
                console.log('Row InSert : '+ result.rowsAffected);
                doRelease(connection, result.rowsAffected);
            });
        });

    function doRelease(connection, result) {
        connection.release(function (err) {
            if (err) {
                console.error(err.message);
            }
            res.send(result);
        })
    }
})

app.all('*', (req,res)=> {
    res.status(404).send('<h1>ERROR - Page is Not Found.</h1>');
});

app.listen(app.get('port'), ()=> {
    console.log("Express Server Listening on port" + app.get('port'));
})
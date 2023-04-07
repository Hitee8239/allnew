const oracledb = require('oracledb');
const dbConfig = require('./dbConfig');

oracledb.getConnection(
    {
        user : dbConfig.user,
        password : dbConfig.password,
        connectString: dbConfig.connectString
    },
    (err, connection)=>{
        if(err){
            console.error(err.message);
            return;
        }
        connection.execute(
            "SELECT * FROM USERTBL",
            (err, rst)=>{
                if(err){
                    console.err(err.message);
                    doRelease(connection);
                    return;
                }
                console.log(rst.metaData);
                console.log(rst.rows);
                doRelease(connection);
            }
        );
    }
);

function doRelease(connection){
    connection.release(
        err => {
            if(err){
            console.error(err.message);
            }
        }
    );
}
const axios = require('axios');

axios
    .post('https://example.com/todos',{
        todo : "Buy the milk"
    })
    .then((res) => {
        console.log(`statusCode : ${res.statusCode}`)
        console.log(res)
    }).catch((err) => {
        console.error(err)
    });
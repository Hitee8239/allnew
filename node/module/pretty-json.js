// 예쁘게 JSON을 뿌려주는 모듈 
const prettier = require('prettier')

res.json(prettier.format(JSON.stringify(object)))

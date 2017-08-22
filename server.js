const http = require('http');
const fs = require('fs');

var contents = fs.readFileSync('sample.json').toString();
// console.log(contents)

const server = http.createServer((req, res) => {



res.end(contents);


});


server.listen(8000);
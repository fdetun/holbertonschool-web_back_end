const http = require('http');

const app = http.createServer((req, rep) => {
  rep.end('Hello Holberton School!');
});

app.listen('127.0.0.1', 1245);
module.exports = app;

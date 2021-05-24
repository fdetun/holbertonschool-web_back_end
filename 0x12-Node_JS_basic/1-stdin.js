const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log('Welcome to Holberton School, what is your name?');
readline.question('', (name) => {
  console.log(`Your name is:${name}`);
  if (!process.stdin.isTTY) {
    console.log('This important software is now closing');
  }
  readline.close();
});

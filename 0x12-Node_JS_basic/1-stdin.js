const readline = require('readline').createInterface({
  input: process.stdin,
});

process.stdout.write('Welcome to Holberton School, what is your name?\n');
readline.question('', (name) => {
  process.stdout.write(`Your name is:${name}\n`);
  if (!process.stdin.isTTY) {
    process.stdout.write('This important software is now closing\n');
  }
  readline.close();
});

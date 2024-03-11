#!/usr/bin/node
const args = process.argv;
const myNumber = Number(args[2])
if (myNumber) {
  console.log(`My number: ${myNumber}`);
}
else {
  console.log('Not a number');
}

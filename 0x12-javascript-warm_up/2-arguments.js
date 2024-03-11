#!/usr/bin/node
const args = process.argv;
if (!args[2]) {
  console.log('No argument');
} else if (args[2] && !args[3]) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

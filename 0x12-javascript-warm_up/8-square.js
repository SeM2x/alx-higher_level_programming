#!/usr/bin/node
const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
}

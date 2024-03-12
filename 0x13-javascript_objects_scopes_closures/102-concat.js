#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

let str = '';

fs.readFile(fileA, 'utf8', (err, data) => {
    if (err) throw err;
    str += data;
});
fs.readFile(fileB, 'utf8', (err, data) => {
    if (err) throw err;
    str += data;
});

fs.writeFile(fileC, str)

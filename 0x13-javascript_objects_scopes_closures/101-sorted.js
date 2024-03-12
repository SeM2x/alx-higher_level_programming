#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

Object.values(dict).forEach((val, index) => {
  newDict[val] += ' ' + (Object.keys(dict)[index]);
});
Object.entries(newDict).forEach(([key, val]) => {
  newDict[key] = val.replace('undefined ', '').split(' ');
});

console.log(newDict);

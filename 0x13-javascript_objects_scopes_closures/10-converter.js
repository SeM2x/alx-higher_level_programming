#!/usr/bin/node
let currentBase = 0;

exports.converter = function (base) {
  currentBase = base;
  return decToBase;
};
const decToBase = (num) => {
  return num.toString(currentBase);
};

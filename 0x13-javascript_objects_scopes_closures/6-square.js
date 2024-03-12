#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let char = c;
    let i = 0;
    if (char === undefined) {
      char = 'X';
    }
    while (i < this.height) {
      console.log(String(char).repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;

#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let = 0;
    while (i < this.height) {
      console.log(String(char).repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;

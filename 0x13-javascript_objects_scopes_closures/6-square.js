#!/usr/bin/node
const SquareC = require('./5-square.js');

class Square extends SquareC {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      console.log(String(c).repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;

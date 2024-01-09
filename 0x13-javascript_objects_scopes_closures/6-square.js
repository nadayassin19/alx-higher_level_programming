#!/usr/bin/node
const superSquare = require('./5-square');

class Square extends superSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0, s; i < this.height; i++) {
      s = '';
      for (let j = 0; j < this.wid; j++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;

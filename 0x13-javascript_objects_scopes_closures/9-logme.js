#!/usr/bin/node
let nOarg = 0;

exports.logMe = function (item) {
  console.log(nOarg + ': ' + item);
  nOarg++;
};

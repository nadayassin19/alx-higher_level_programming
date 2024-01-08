#!/usr/bin/node
const myArg = process.argv[2];
const myArgInt = Number(myArg);
console.log(myArgInt === NaN ? 'Not a number' : 'My number:' + myArgInt);

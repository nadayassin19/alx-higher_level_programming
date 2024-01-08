#!/usr/bin/node
const myArg = parseInt(process.argv[2]);
console.log(myArg === NaN ? 'Not a number' : 'My number: ' + myArg);

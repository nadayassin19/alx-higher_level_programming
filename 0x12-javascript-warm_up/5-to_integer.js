#!/usr/bin/node
const myArg = parseInt(process.argv[2]);
console.log(Number.isNaN(myArg) ? 'Not a number' : 'My number: ' + myArg);

#!/usr/bin/node
myArg = process.number(argv[2]);
console.log(myArg === NaN ? 'Not a number' : 'My number:' + myArg);

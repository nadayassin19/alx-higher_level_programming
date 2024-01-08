#!/usr/bin/node
const myArg = process.argv.length;
console.log(myArg == 1 ? 'Argument found' : myArg > 1 ? 'Arguments found' : 'No argument');

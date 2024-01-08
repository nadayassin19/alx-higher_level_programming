#!/usr/bin/node
const myArg = process.argv.length;
console.log(myArg > 3 ? 'No argument' : myArg === 3 ? 'Argument found' : 'Arguments found');

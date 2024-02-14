#!/usr/bin/node
const sF = require('fs');

const fArg = sF.readFileSync(process.argv[2]).toString();
const sArg = sF.readFileSync(process.argv[3]).toString();
sF.writeFileSync(process.argv[4], fArg + sArg);

#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[4]);
if (Number.isNaN(a) || Number.isNaN(b)) {
  console.log(NaN);
} else {
  const c = a + b;
  console.log(c);
}

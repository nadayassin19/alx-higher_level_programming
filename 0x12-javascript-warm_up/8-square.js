#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (Number.isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0, s; i < x; i++) {
    s = '';
    for (let j = 0; j < x; j++) {
      s += 'X';
    }
    console.log(s);
  }
}

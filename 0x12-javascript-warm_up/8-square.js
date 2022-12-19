#!/usr/bin/node
// prints a square
const num = Math.floor(Number(process.argv[2]));
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let rows = 0; rows < num; rows++) {
    let row = '';
    for (let cols = 0; cols < num; cols++) {
      row += 'X';
    }
    console.log(row);
  }
}

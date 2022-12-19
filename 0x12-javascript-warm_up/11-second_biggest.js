#!/usr/bin/node
// searches second biggest integer in list of args
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const numList = [];
  for (let i = 2; i < process.argv.length; i++) {
    numList[i - 2] = Number(process.argv[i]);
  }
  numList.sort().reverse();
  console.log(numList[1]);
}

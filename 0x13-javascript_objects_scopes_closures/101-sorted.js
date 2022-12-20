#!/usr/bin/node
const dict = require('./101-data').dict;
let myDict = {};
for (let key in dict) {
  if (myDict[dict[key]] === undefined) {
    myDict[dict[key]] = [key];
  } else {
    myDict[dict[key]].push(key);
  }
}
console.log(myDict);

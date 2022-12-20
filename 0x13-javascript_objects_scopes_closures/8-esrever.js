#!/usr/bin/node

exports.esrever = function (list) {
  let myList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    myList.push(list[i]);
  }
  return myList;
};

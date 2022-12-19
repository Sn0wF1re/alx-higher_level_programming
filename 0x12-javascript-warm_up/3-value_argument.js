#!/usr/bin/node
/* prints the first argument passed to it */
console.log(process.argv[2] === undefined ? 'No argument' : process.argv[2]);

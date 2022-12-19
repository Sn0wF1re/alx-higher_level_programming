#!/usr/bin/node
/* prints the first argument passed to it */
const argLength = process.argv.length;
console.log(argLength === 2 ? 'No argument' : process.argv[2]); 

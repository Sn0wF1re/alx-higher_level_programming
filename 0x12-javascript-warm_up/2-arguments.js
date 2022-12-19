#!/usr/bin/node
/* prints a message depending of the number of arguments passed */
argLength = process.argv.length;
if (argLength == 2) {
  console.log('No argument');
}
else if (argLength == 3){
  console.log('Argument found');
}else {
  console.log('Arguments found');
}

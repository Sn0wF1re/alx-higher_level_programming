#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filepath, data, (err) => {
  if (err) console.log(err);
});

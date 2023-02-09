#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    const index = films.length - 1;
    for (let i = 0; i <= index; i++) {
      const chars = films[i].characters;
      for (const charIndex in chars) {
        if (chars[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Error: ' + response.statusCode);
  }
});

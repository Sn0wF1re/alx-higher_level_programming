#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    tasks.forEach((task) => {
      if (task.completed && completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else if (task.completed) {
        completed[task.userId]++;
      }
    });
    console.log(completed);
  }
});

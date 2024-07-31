#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const tasks = JSON.parse(response.body);
    const res = {};
    tasks.forEach((task) => {
      if (task.completed) { res[task.userId] = (res[task.userId] | 0) + 1; }
    });
    console.log(res);
  }
});

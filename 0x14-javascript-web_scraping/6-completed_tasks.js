#!/usr/bin/node
/* List tasks */
const request = require('request');
const url = process.argv[2];

request(url, function (err, resp, body) {
  if (err) {
    console.log(err);
  } else {
    const dic = {};
    const data = JSON.parse(body);
    for (const i of data) {
      if (i.completed === true) {
        if (i.userId in dic) {
          dic[i.userId] += 1;
        } else {
          dic[i.userId] = 1;
        }
      }
    }
    console.log(dic);
  }
});

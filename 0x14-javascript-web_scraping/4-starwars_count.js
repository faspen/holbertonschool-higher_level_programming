#!/usr/bin/node
/* Find Wedge */

const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let num = 0;
    for (const i in movies) {
      const chars = movies[i].characters;
      for (const j in chars) {
        if (chars[j].includes('18')) {
          num++;
        }
      }
    }
    console.log(num);
  }
});

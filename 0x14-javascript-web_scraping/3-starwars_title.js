#!/usr/bin/node
/* Star wars */

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const movie = process.argv[2];
request(url + movie, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const tmp = JSON.parse(body);
    console.log(tmp.title);
  }
});

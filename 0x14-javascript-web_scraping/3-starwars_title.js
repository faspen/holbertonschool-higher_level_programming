#!/usr/bin/node
/* Star wars */

const request = require('request');

let url = 'https://swapi-api.hbtn.io/api/films/';
let movie = process.argv[2];
request(url + movie, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let tmp = JSON.parse(body);
    console.log(tmp.title);
  }
});

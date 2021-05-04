#!/usr/bin/node
/* Star wars */

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
const movie = process.argv[2];
request(url + movie, function (err, response, body) {
    console.log(err || JSON.parse(body).title);
});

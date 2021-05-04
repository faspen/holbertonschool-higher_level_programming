#!/usr/bin/node
/* Store webpage in file */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const f = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(f, body);
  }
});

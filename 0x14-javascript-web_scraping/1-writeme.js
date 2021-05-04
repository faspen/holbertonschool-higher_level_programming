#!/usr/bin/node
/* Write to file */

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  }
});

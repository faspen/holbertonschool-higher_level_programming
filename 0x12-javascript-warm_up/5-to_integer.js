#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (Number.isInteger(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}

#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (Number.isInteger(num)) {
  console.log(num);
} else {
  console.log('Not a number');
}

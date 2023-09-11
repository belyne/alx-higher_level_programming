#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (size > 0) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else if (size === 0 || isNaN(size)) {
  console.log('Missing size');
}

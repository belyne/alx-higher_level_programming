#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from command line argument
const content = process.argv[3]; // Get the content from command line argument

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred
  }
});

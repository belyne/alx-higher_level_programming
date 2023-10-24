#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL from command line argument
const filePath = process.argv[3]; // Get the file path from command line argument

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred
  } else {
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err); // Print the error object if an error occurred while writing
      }
    });
  }
});

#!/usr/bin/node

const request = require('request');

const url = process.argv[2]; // Get the URL from command line argument

request.get(url, (error, response) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred
  } else {
    console.log(`code: ${response.statusCode}`); // Print the status code
  }
});

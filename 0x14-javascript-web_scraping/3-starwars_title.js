#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2]; // Get the movie ID from command line argument
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`; // URL with movie ID

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title); // Print the title of the movie
  }
});

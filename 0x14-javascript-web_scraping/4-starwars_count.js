#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line argument
const characterId = 18; // Character ID for "Wedge Antilles"

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred
  } else {
    const filmsData = JSON.parse(body);
    const filmsWithWedgeAntilles = filmsData.results.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(filmsWithWedgeAntilles.length); // Print the number of movies with Wedge Antilles
  }
});

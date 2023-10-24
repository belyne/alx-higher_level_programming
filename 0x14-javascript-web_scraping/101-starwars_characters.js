#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2]; // Get the movie ID from command line argument
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`; // URL with movie ID

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred
  } else {
    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    const characterPromises = characterUrls.map(url =>
      new Promise((resolve, reject) => {
        request.get(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      })
    );

    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(error => console.error(error));
  }
});

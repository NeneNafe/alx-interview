#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const APIUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(APIUrl, async function (error, response, body) {
  if (error) return console.error(error);

  // Parses the response body to get the character list
  const charList = JSON.parse(body).characters;

  // Iterate through the char list to fetch a film title
  const fetchCharName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) return console.error(error);

        // Returns the name of the called film
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  };

  try {
    await Promise.all(charList.map(url => fetchCharName(url)));
  } catch (error) {
    console.error(error);
  }
});

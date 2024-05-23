#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const APIUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(APIUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach(characterUrl => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.log(charError);
        return;
      }

      const charData = JSON.parse(charBody);
      console.log(charData.name);
    });
  });
});

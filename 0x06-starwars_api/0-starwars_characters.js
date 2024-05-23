#!/usr/bin/node
const { error } = require('console');
const request = require('request');

const movieId = process.argv[2];
const APIUrl = 'https://swapi-api.hbtn.io/api/films/' + movieId;

function sendRequest (charList, indx) {
  if (charList.length === indx) {
    return;
  }

  request(charList[indx], (err, res, body) => {
    if (err) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(charList, indx + 1);
    }
  });
}

request(APIUrl, (err, res, body) => {
  if (err) {
    console.log(error);
  } else {
    const charList = JSON.parse(body).characters;

    sendRequest(charList, 0);
  }
});

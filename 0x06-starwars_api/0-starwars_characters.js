#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const api = 'https://swapi.dev/api/';
const url = api + 'films/' + movieId + '/';
request.get({ url }, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    order(characters);
  } else {
    console.error('Failed to fetch movie data:', error);
  }
});

function order (characters) {
  if (characters.length > 0) {
    const characterUrl = characters.shift();
    request.get({ url: characterUrl }, function (error, response, body) {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        order(characters);
      } else {
        console.error('Failed to fetch character data:', error);
      }
    });
  }
}

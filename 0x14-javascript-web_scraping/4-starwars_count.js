#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const films = JSON.parse(response.body).results;
    console.log(films.reduce((count, film) => {
      if (film.characters.find((character) => character.endsWith('/18/'))) {
        return count + 1;
      }
      return count;
    }, 0));
  }
});

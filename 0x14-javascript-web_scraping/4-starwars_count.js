#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api';
const url = `${api}/films`;
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(response.body).results;
    const count = films.reduce((count, film) => {
      if (film.characters?.indexOf(`${api}/people/18/`) !== -1) {
        return count + 1;
      }
      return count;
    }, 0);
    console.log(count);
  }
});

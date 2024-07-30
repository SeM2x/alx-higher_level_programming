#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api';
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    if (response.statusCode === 200) {
      const films = JSON.parse(response.body).results;
      const count = films?.reduce((count, film) => {
        if (film.characters?.indexOf(`${api}/people/18/`) !== -1) {
          return count + 1;
        }
        return count;
      }, 0);
      if (count !== undefined) {
        console.log(count);
      } else {
        console.log(0);
      }
    }
  }
});

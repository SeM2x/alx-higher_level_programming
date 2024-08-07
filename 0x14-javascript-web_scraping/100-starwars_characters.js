#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(response.body).characters;
    characters.forEach(character =>
      request(character, (error, response, body) => {
        if (!error) {
          console.log(JSON.parse(response.body).name);
        }
      })
    );
  }
});

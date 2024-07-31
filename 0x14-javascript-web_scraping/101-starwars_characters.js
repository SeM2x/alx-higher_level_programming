#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(response.body).characters;
    const res = [];
    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const character = JSON.parse(response.body);
          const index = character.url.substring(0, character.url.length - 1).substring(character.url.length - 3);
          res.push({
            name: character.name,
            index: index.startsWith('/') ? +index.substring(1) : +index
          });
          if (characters.length === res.length) {
            res.sort((a, b) => a.index - b.index);
            res.forEach(char => console.log(char.name));
          }
        }
      });
    });
  }
});

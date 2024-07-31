#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(response.body).characters;
    const res = [];
    characters.forEach(character => {
      request(character, (error, response, body) => {
        if (!error) {
          const result = JSON.parse(response.body);
          const index = result.url.substring(0, result.url.length - 1).substring(result.url.length - 3);
          res.push({
            name: result.name,
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

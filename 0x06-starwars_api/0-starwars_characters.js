#!/usr/bin/node

const request = require('request');
const args = process.argv;
const obj = {};
const url = `https://swapi-api.alx-tools.com/api/films/${args[2]}`;
request(url, (error, response, body) => {
  if (error) console.error('error:', error);
  const data = JSON.parse(body);
  getName(data.characters);
});

const getName = async (content) => {
  for (const i in content) {
    request(content[i], (error, response, body) => {
      if (error) console.error('error:', error);
      const data = JSON.parse(body);
      obj[i] = data.name;
    });
  }
};

// cheat async await
setTimeout(() => {
  for (const i in obj) {
    console.log(obj[i]);
  }
}, 5000);

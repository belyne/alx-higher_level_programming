#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line argument

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error object if an error occurred
  } else {
    const todosData = JSON.parse(body);
    const completedTasks = {};

    todosData.forEach(task => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  }
});

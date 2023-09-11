#!/usr/bin/node

function secondBiggest (args) {
  args = args.map(Number);
  args = args.sort((a, b) => b - a);
  if (args.length <= 2) {
    return 0;
  }
  return args[1];
}

const args = process.argv.slice(2);

console.log(secondBiggest(args));

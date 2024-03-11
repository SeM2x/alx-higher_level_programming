#!/usr/bin/node
const factorial = (x) => {
  if (!x) {
    return 1;
  }
  return x * factorial(x - 1);
}

const x = Number(process.argv[2]);
console.log(factorial(x));

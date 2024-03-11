#!/usr/bin/node
let args = process.argv.slice(2).map(arg => Number(arg));
if (args.length < 2) {
  console.log(0);
} else {
  let max = args[0];
  args.forEach(element => {
    if (element > max) {
      max = element;
    }
  });
  args = args.filter(element => element != max);
  max = args[0];
  args.forEach(element => {
    if (element > max) {
      max = element;
    }
  });
  console.log(max);
}

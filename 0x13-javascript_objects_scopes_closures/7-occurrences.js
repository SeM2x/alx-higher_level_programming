#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return (
    list.reduce((acc, current) => {
      if (current === searchElement) {
        return acc + 1;
      }
      return acc;
    }, 0)
  );
}
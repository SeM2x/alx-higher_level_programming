#!/usr/bin/node
exports.esrever = function (list) {
  if (list.length <= 1) {
    return list;
  }
  const first = list.shift();
  const last = list.pop();
  exports.esrever(list);
  list.push(first);
  list.unshift(last);
  return list;
};

function atm(num, times) {
  times.sort();
  let total = 0;
  let result = 0;

  for (let i = 0; i < num; i++) {
    total += times[i];
    result += total;
  }

  return result;
}

console.log(atm(5, [3, 1, 4, 3, 2]));

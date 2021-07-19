function solution(n, lost, reserve) {
  let tmpLost = lost.slice();
  let tmpReserve = reserve.splice();

  for (const i of tmpLost) {
    for (const j of tmpReserve) {
      if (i === j) {
        lost.splice(tmpLost.indexOf(i), 1);
        reserve.splice(tmpReserve.indexOf(j), 1);
      }
    }
  }

  for (let i of reserve) {
    let key = lost.includes(i - 1) ? lost.indexOf(i - 1) : lost.indexOf(i + 1);
    if (key !== -1) {
      lost.splice(key, 1);
    }
  }

  return n - lost.length;
}

console.log(solution(6, [2, 4, 6], [1, 3, 5, 6]));
console.log(solution(5, [2, 4], [1, 3, 5]));
console.log(solution(5, [2, 4], [3]));
console.log(solution(3, [3], [1]));

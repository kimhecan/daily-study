function solution(participant, completion) {
  let obj = {};
  for (const i of participant) {
    if (obj[i] !== undefined) {
      obj[i] += 1;
    } else {
      obj[i] = 1;
    }
  }

  for (const i of completion) {
    obj[i] -= 1;
  }
  for (const i of participant) {
    if (obj[i] !== 0) return i;
  }
}

console.log(
  solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
);

function solution(participant, completion) {
  let dic = completion.reduce(
    (acc, cur) => ((acc[cur] = acc[cur] ? acc[cur] + 1 : 1), acc),
    {}
  );

  return participant.find((value) => {
    if (dic[value]) {
      dic[value] -= 1;
    } else {
      return true;
    }
  });
}

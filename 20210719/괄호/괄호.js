function solution(expression) {
  let expressionList = expression.split("-");
  let total = 0;

  for (let i = 0; i < expressionList.length; i++) {
    if (i == 0) {
      total += expressionList[i]
        .split("+")
        .reduce((acc, cur) => parseInt(acc) + parseInt(cur));
    } else {
      total -= expressionList[i]
        .split("+")
        .reduce((acc, cur) => parseInt(acc) + parseInt(cur));
    }
  }

  console.log(total);
}

solution("55-50+40");

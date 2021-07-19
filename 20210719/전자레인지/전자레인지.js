function solution(time) {
  let countList = [0, 0, 0];
  let buttonList = [300, 60, 10];

  for (let i = 0; i < buttonList.length; i++) {
    if (buttonList[i] <= time) {
      countList[i] = parseInt(time / buttonList[i]);
      time = time % buttonList[i];
    }
  }

  if (time === 0) {
    console.log(countList);
  } else {
    console.log(-1);
  }
}

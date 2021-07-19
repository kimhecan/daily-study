function solution(n, k, coinList) {
  let count = 0;
  coinList.reverse();

  for (const i of coinList) {
    if (i <= k) {
      count += parseInt(k / i);
      k = k % i;
    }
    if (k == 0) {
      console.log(cout);
      break;
    }
  }
}

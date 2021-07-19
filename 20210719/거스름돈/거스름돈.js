function solution(n) {
  let returnCoin = 1000 - n;
  let coins = [500, 100, 50, 10, 5, 1];
  let count = 0;

  for (const coin of coins) {
    if (coin <= returnCoin) {
      count += paseInt(returnCoin / coin);
    }
  }
  print(count);
}

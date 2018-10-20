const BigNumber = require('bignumber.js');


function getFibonacciSum(num) {
  num = new BigNumber(num);

  let result = new BigNumber(0);
  let previous = new BigNumber(0);
  let current = new BigNumber(1);
  let mid;
  
  while (previous.plus(current).isLessThan(num)) {
    mid = previous.plus(current);

    previous = current;
    current = mid;

    if (current.modulo(2).isEqualTo(0)) {
      result = result.plus(current);
    }
  }
  return result;
}

module.exports = getFibonacciSum;

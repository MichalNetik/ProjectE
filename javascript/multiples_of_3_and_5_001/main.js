const BigNumber = require('bignumber.js');

function getSumOfSingleMultiplier(num, multiplier) {
  const num_over_multiplier = new BigNumber(num).dividedToIntegerBy(multiplier);
  return num_over_multiplier
    .multipliedBy(multiplier)
    .multipliedBy(num_over_multiplier.plus(1))
    .dividedToIntegerBy(2);
}

function getMultipliesSum(num) {
  num = num - 1;

  let result = new BigNumber(0);

  result = result.plus(getSumOfSingleMultiplier(num, 3));
  result = result.plus(getSumOfSingleMultiplier(num, 5));
  result = result.minus(getSumOfSingleMultiplier(num, 15));
  return result;
}

module.exports = getMultipliesSum;

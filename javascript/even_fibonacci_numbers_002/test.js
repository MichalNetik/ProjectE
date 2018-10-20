const expect = require('chai').expect;
const getFibonacciSum = require('./main');


describe('getFibonacciSum(num)', () => {
  it('Should return 10 for num = 10', () => {
    const num = 10;
    const result = getFibonacciSum(num);

    expect(result.toString()).to.be.equal('10');
  });

  it('Should return 44 for num = 100', () => {
    const num = 100;
    const result = getFibonacciSum(num);

    expect(result.toString()).to.be.equal('44');
  });
});

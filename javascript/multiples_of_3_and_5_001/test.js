const expect = require('chai').expect;
const getMultipliesSum = require('./main');


describe('getMultipliesSum()', function () { 
  it('Should return 23 for num = 10', () => {
    const num = 10;
    const result = getMultipliesSum(num);

    expect(result.toString()).to.be.equal('23');
  });

  it('Should return 2318 for num = 100', () => {
    const num = 100;
    const result = getMultipliesSum(num);

    expect(result.toString()).to.be.equal('2318');
  });

  it('Should return 233168 for num = 1000', () => {
    const num = 1000;
    const result = getMultipliesSum(num);

    expect(result.toString()).to.be.equal('233168');
  });

  it('Should return 2333316668 for num = 100000', () => {
    const num = 100000;
    const result = getMultipliesSum(num);

    expect(result.toString()).to.be.equal('2333316668');
  });

  it('Should return 2333316668 for num = 10000000', () => {
    const num = 10000000;
    const result = getMultipliesSum(num);

    expect(result.toString()).to.be.equal('23333331666668');
  });
});

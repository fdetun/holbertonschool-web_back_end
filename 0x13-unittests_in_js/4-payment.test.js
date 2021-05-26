const sendPaymentRequestToApi = require('./3-payment.js');
const Util = require('./utils');
const assert = require('assert');
const sinn = require('sinon');

describe('test with spy', function() {
    it('check0', function() {
        const c = sinn.spy(console, 'log');
        const a = sinn.stub(Util, 'calculateNumber').returns(10);
        sendPaymentRequestToApi(100, 20);
        assert.ok(a.calledWithExactly('SUM', 100, 20), true);
        assert.ok(c.calledWithExactly("The total is: 10"), true);
        a.restore();
        c.restore();
    });
});
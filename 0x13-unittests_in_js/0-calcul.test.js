const calculateNumber = require("./0-calcul");
const assert = require('assert');

describe("calculate number testing", () => {

    it('test1', function() {
        assert.strictEqual(calculateNumber(4, 2.8), 7);
    });
    it('test2', function() {
        assert.ok(!(calculateNumber(0, 0)));
    });
    it('test3', function() {
        assert.ok(!(calculateNumber("str", 100, 2.9)));
    });
    it('test4', function() {
        assert.ok(!(calculateNumber({}, "str")));
    });

});
/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    // Easy

    return function(x) {
        for (let el = functions.length-1; el >= 0; el--) {
            x = functions[el](x);
        }
        return x
    }
};
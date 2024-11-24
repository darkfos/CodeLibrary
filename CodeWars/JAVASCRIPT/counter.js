/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    // Easy

    let cnt = n;
    return function() {
        if (cnt === n) {
            cnt++;
            return n
        } else {
            let prev = cnt;
            cnt++;
            return prev
        }
    };
};
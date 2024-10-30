/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    /*
        Easy
        Given an integer n, return true if it is a power of two. Otherwise, return false.
        An integer n is a power of two, if there exists an integer x such that n == 2x.
    */
    
    for (let cnt = 0; cnt < n+1; cnt++) {
        if (2**cnt === n) {
            return true
        } else if (2**cnt > n) {
            break;
        }
    }
    return false;
};
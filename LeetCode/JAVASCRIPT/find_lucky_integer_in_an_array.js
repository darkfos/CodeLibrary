/**
    Given an array of integers arr, a lucky integer is an
    integer that has a frequency in the array equal to
    its value.
    Return the largest lucky integer in the array. If
    there is no lucky integer return -1.
*/

/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    // Easy
    
    let luckyNumbers = new Array();
    arr.map((el) => {
        if (countElement(arr, el) === el) {
            luckyNumbers.push(
                el
            )
        }
    })

    let result = Math.max(...luckyNumbers);
    switch (result) {
        case -Infinity:
            return -1;
        default:
            return result
    }
};


let countElement = (arr, el) => {
    let cnt = 0;
    
    arr.forEach(element => {
        if (element === el) {
            cnt++
        } 
    });

    return cnt
}
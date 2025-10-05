/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 * Medium level
 * https://leetcode.com/problems/flatten-deeply-nested-array/description/
 */
var flat = function (arr, n) {

    if (n === 0) {
        return arr
    }

    const flattenArray = [];

    for (let el of arr) {
        if (Array.isArray(el) && n > 0) {
            flattenArray.push(...flat(el, n-1))
        } else {
            flattenArray.push(el)
        }
    }

    return flattenArray
}

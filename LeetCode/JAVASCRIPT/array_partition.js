/*
    Given an integer array nums of 2n integers, group these integers into n pairs
    (a1, b1), (a2, b2), ...,  (an, bn) such that the sum of min(ai, bi) for all i
    is maximized. Return the maximized sum.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    // Easy
    nums.sort((el1, el2) => el1 - el2);
    let result = 0;
    for (let el = 0; el < nums.length; el += 2) {
        result += nums[el];
    }
    return result
};
/*
    Given an unsorted array of integers nums, return the length of the longest continuous
    increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

    A continuous increasing subsequence is defined by two indices l and r (l < r) such
    that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    // Easy

    let maxSequence = 0;
    let cntLocal = 1;

    for (let number1 = 0; number1 < nums.length; number1++) {
        if (cntLocal > maxSequence) {
            maxSequence = cntLocal;
        }

        if (nums[number1] < nums[number1+1]) {
            cntLocal++;
        } else {
            cntLocal = 1;
        }

    }

    return maxSequence
};
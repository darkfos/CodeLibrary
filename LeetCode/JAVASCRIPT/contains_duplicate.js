/*
    Given an integer array nums, return true if any value appears
    at least twice in the array, and return false if every element is distinct.
*/

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // Easy

    let set_array = new Set(nums);

    return set_array.size !== nums.length;
};
/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    /**
     * EASY
     * You are given a sorted unique integer array nums.
        A range [a,b] is the set of all integers from
        a to b (inclusive).
        Return the smallest sorted list of ranges that cover
        all the numbers in the array exactly. That is, each element
        of nums is covered by exactly one of the ranges, and there is
        no integer x such that x is in one of the ranges but not in nums.
     */

    if (nums.length === 0) {
        return [];
    }

    let prev;
    let next;
    let result = new Array();

    nums.forEach((el, indx) => {
        if (prev === undefined) {
            prev = el;
            next = prev;
        } else {
            if (nums[indx] === next+1) {
                next = nums[indx];
            } else {
                result.push(prev !== next? `${prev}->${next}`: `${prev}`);
                prev = nums[indx];
                next = prev;
            }
        }
    })

    if (next === prev) {
        result.push(`${next}`);
    } else {
        result.push(`${prev}->${next}`)
    }

    return result;
};
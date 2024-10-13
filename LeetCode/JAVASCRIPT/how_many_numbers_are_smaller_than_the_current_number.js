/*
    Given the array nums, for each nums[i] find out
    how many numbers in the array are smaller than
    it. That is, for each nums[i] you have to count
    the number of valid j's such that j != i and
    nums[j] < nums[i].

    Return the answer in an array.
*/

/**
 * 
 *  @param {number[]} nums
 *  @param {numbers[]}
 */
var smallerNumbersThanCurrent = function (nums) {
    // Easy

    let countNumsArray = new Array();
    nums.map((el, indx) => {
        countNumsArray.push(
            nums.filter((el2) => {
                return el2 < el
            }).length
        )
    })

    return countNumsArray
}
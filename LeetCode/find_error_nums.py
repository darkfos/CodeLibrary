from typing import List

"""
    You have a set of integers s, which originally contains all the numbers from 1 to n.
    Unfortunately, due to some error, one of the numbers in s got duplicated to another
    number in the set, which results in repetition of one number and loss of another number.
    
    You are given an integer array nums representing the data status of this set after the error.
    
    Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""


#Set Mismatch
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #Easy

        nums = sorted(nums)
        res: list = []
        check_number: int = 0
        for number in range(len(nums)):
            if nums.count(nums[number]) > 1:
                if check_number == 0:
                    res.append(nums[number])
                check_number += 1
                if check_number == 2:
                    find_numbers = list(filter(lambda x: x not in nums, range(1, max(nums)+2)))
                    if find_numbers:
                        res.append(find_numbers[0])
                    else:
                        res.append(res[-1]+1)
                    return res
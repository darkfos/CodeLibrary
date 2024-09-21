from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_length: int = 0
        max_number: int = 0
        index_start: int = 0
        length_nm: int = 0
        index_end: int = 0
        for number in set(nums):
            if nums.count(number) >= max_length:
                res = self.find_end_number(
                    max_number=number,
                    nums=nums,
                )
                if res >= index_end or length_nm == 0:
                    max_length = nums.count(number)
                    max_number = number
                    index_start = nums.index(number)
                    index_end = self.find_end_number(max_number=max_number,
                                                    nums=nums)
                    length_nm = self.sm_numbers(index_start=index_start, index_end=index_end)
        return length_nm

    def find_end_number(self, max_number: int, nums: list) -> int:

        index_max_number: int = 0

        #Find index end number
        for number in range(len(nums)-1, 0, -1):
            if nums[number] == max_number:
                index_max_number = number
                break

        #Sum elements
        return index_max_number

    def sm_numbers(self, index_start: int, index_end) -> int:
        return sum([1 for _ in range(index_start, index_end+1)])

test = Solution().findShortestSubArray(nums=[1,2,2,3,1,4,2])
print(test)

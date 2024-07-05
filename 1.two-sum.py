from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for ii in range(length - 1):
            a = nums[ii]
            for jj in range(ii + 1, length):
                b = nums[jj]
                sums = a + b
                if target == sums:
                    ans = [ii, jj]
                    return ans
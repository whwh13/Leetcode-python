from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)-nums[0]
        for ii in range(0,len(nums)):
            if left == right:
                return ii
            elif ii == len(nums)-1:
                return -1
            else:
                left += nums[ii]
                right -= nums[ii+1]

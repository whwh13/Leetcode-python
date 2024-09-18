from typing import List

# 没有写完
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        ans=nums[0]+nums[1]+nums[2]
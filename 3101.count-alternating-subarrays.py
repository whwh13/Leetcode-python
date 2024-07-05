from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 1
        last_pos=0
        all_sub=0
        for jj in range(1,n):
            if nums[jj]==nums[jj-1]:
                all_sub += (jj-last_pos)*(jj-last_pos+1)//2
                last_pos=jj
        all_sub += (n-last_pos)*(n-last_pos+1)//2

        return all_sub
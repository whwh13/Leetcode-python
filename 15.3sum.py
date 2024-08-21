from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        for i in range(0,len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue    
            k = n-1
            for j in range(i+1,len(nums)-1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                while nums[i] + nums[j] + nums[k]>0 and k>j:
                    k -= 1
                if k<=j:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    ans += [[nums[i],nums[j],nums[k]]]

        return ans
    
# 看了题解
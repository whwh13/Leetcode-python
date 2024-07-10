from typing import List
# 太过暴力了

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        l=len(nums)
        n=0
        for ii in range(0,l):
            for jj in range(ii,l):
                if self.judge(nums,ii,jj):
                    n += 1
        return n
    
    def judge(self,nums,ii,jj):
        k=nums[:ii] + nums[jj+1:]
        if len(k)==0 or len(k)==1:
            return True
        for tt in range(1,len(k)):
            if k[tt]-k[tt-1]<=0:
                return False
        return True
    
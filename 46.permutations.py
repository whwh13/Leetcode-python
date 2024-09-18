from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        if n==1:
            return [nums]
        for ii in range(0,n):
            k=self.permute(nums[:ii] + nums[ii+1:])
            for sublist in k:
                sublist += [nums[ii]]
            ans += k
        return ans
nums=[1,2,3]

solution = Solution()
print(solution.permute(nums))
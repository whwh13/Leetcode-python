from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums=self.sort(nums)
        for i in range(0, len(nums), 2):
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
        return nums


    def sort(self, nums):
        for jj in range(len(nums)):
            t=nums[jj]
            for kk in range(jj,0,-1):
                if t>=nums[kk-1]:
                    nums[kk+1:jj+1]=nums[kk:jj]
                    nums[kk]=t
                    break
                elif kk==1:
                    nums[1:jj+1]=nums[0:jj]
                    nums[0]=t
                    break
        return nums


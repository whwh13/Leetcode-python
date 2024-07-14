from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n=len(nums)
        left=True
        right=True
        ii=0
        while left or right:
            if left and self.is_prime(nums[ii]):
                left = False
                leftNum=ii
            if right and self.is_prime(nums[n-1-ii]):
                right = False
                rightNum=n-1-ii
            ii += 1
        return rightNum-leftNum

    def is_prime(self,n): # chatgpt解决的
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
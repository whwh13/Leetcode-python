from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        count_now=0
        max_last=0
        max_now=0
        for ii in nums:
        
            if bin(ii).count('1')==count_now:
                if ii>max_now:
                    max_now=ii
            else:
                count_now=bin(ii).count('1')
                max_last=max_now
                max_now=ii

            if ii<max_last:
                return False
        return True
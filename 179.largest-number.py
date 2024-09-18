from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ans=""
        nums.sort(reverse=True)
        n100=0
        while n100<=len(nums)-1 and nums[n100]==100:
            n100 += 1
        nums = nums[n100:]
        nums1=[]
        for i in range(0,len(nums)):
            if nums[i]<10:
                nums1=nums[i:]
                nums=nums[:i]
                break
        p=0
        lp=len(nums1)
        q=0
        lq=len(nums)
        while p<=lp-1 and q<=lq-1:
            if nums[q] // 10 > nums1[p]:
                ans += str(nums[q])
                q += 1
            else:
                if nums[q] // 10 == nums1[p] and nums[q] % 10 >= nums1[p]:
                    ans += str(nums[q])
                    q += 1
                else:
                    ans += str(nums1[p])
                    p += 1
        if p==lp:
            numst=nums
            t=q
            lt=lq
        else:
            numst=nums1
            t=p
            lt=lp
        while t<=lt-1:
            ans += str(numst[t])
            t += 1
        while n100>0:
            ans += str(100)
            n100 -= 1
        return ans

nums = [10]

solution = Solution()
print(solution.largestNumber(nums))
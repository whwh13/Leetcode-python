from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)

        if 0==m:
            return get_mid(n,nums2)
        elif 0==n:
            return get_mid(m,nums1)
        else:
            q=get_mid(n,nums2)
            p=get_mid(m,nums1)
            if p==q:
                return p
            elif q>p:
                temp=nums1
                nums1=nums2
                nums2=temp
                temp=m
                m=n
                n=temp
                temp=p
                p=q
                q=temp
            
            t=min(m,n)//2
            if t==0:
                if n==1:
                    if (m+n) % 2:
                        return float(max(nums2[0],nums1[(m//2)-1]))
                    elif m==n:
                        return (p+q)/2
                    else:
                        return (max(nums2[0],nums1[(m-3)//2])+nums1[(m-1)//2])/2
                else:
                    if (m+n) % 2:
                        return float(min(nums1[0],nums2[(n//2)]))
                    elif m==n:
                        return (p+q)/2
                    else:
                        return (min(nums1[0],nums2[(n+1)//2])+nums2[(n-1)//2])/2
            if m==2 and n==2: 
                if nums1[1]>=nums2[1]:
                    if nums1[0]>=nums2[0]:
                        return (nums1[0]+nums2[1])/2
                    else:
                        return (nums2[0]+nums2[1])/2
                else:
                    return (max(nums1[0],nums2[0])+nums1[1])/2
                    
            nums1=nums1[:-t]
            nums2=nums2[t:]
            return self.findMedianSortedArrays(nums1,nums2)
            

def get_mid(m,num): # 预计会高频使用，不考虑0的情况
    if m % 2:
        return float(num[(m-1)//2])
    else:
        return (num[(m//2)-1]+num[m//2])/2



class lengthpoint:
    def __init__(self, val=0, point=None):
        lengthpoint.val=val
        lengthpoint.point=point

class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        maxlength=lengthpoint(0)

        for ii in range(0,l):
            p = 1
            isEven = False  # 重复字符串是奇数还是偶数
            midNumber = ii
            length=1

            while midNumber >=1 and s[midNumber]==s[midNumber-1]:     # 这里改成递归寻找相同的字符               
                midNumber = midNumber-1
                length=length+1
                p=p+1*isEven
                isEven = not isEven

            midNumber=midNumber+length//2-1*isEven
            
            while 1:
                if midNumber-p>=0 and midNumber+p+isEven<l:
                    if s[midNumber-p]==s[midNumber+p+isEven]:
                        length=length+2
                        p=p+1
                    else:
                        break
                else:
                    break

            if length > maxlength.val:
                maxlength.val = length
                maxlength.point=midNumber

        if maxlength.val % 2:
            return s[maxlength.point-maxlength.val//2:maxlength.point+maxlength.val//2+1]
        else:
            return s[maxlength.point-maxlength.val//2+1:maxlength.point+maxlength.val//2+1]

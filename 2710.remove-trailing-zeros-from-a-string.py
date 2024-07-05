class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        l=len(num)
        while num[l-1]=="0":
            num=num[:-1]
            l=len(num)

        return num
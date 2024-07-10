# 可以修改，采用索引而不是将字符串前缀删除，会快一些，但是懒得改了
class Solution:
    def myAtoi(self, s: str) -> int:

        while s and s[0] == ' ':
            s=s[1:]

        sign = 1
        if s and s[0] == '-':
            sign = -1
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]
        x=0

        while s and s[0].isdigit():
            x=x*10+int(s[0])
            s=s[1:]
        
        if x>2147483647:
            if sign==1:
                return 2147483647
            else:
                return -2147483648
        return sign*x
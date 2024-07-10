class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        if x<10:
            return True
        if x%10==0:
            return False
    

        t=0
        while x//10: 
            
            t=t*10+x%10
            x=x//10
            if t==x:
                return True
            elif t==x//10:
                return True
            elif t>x:
                return False

        return False
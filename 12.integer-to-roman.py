class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        [temp,num]=divmod(num,1000)
        while temp > 0:
            roman += 'M'
            temp -= 1

        str_roman1=['C','D','M']
        str_roman2=['X','L','C']
        str_roman3=['I','V','X']

        [temp,num]=divmod(num,100)
        roman = self.shang(temp,roman,str_roman1)
        [temp,num]=divmod(num,10)
        roman = self.shang(temp,roman,str_roman2)
        roman = self.shang(num,roman,str_roman3)
        return roman    
    def shang(self,shang,roman,str_roman):
        if shang <= 3:
            roman += str_roman[0] * shang
        elif shang == 4:
            roman += str_roman[0] + str_roman[1]
        else:
            shang -= 5
            if shang <= 3:
                roman += str_roman[1] + str_roman[0] * shang
            else:
                roman += str_roman[0] + str_roman[2]
        return roman
    
num = 3749
solution = Solution()
print(solution.intToRoman(num))
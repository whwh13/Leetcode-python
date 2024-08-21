from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        public_str=''
        length = len(min(strs, key=len))
        for j in range(0,length):
            for i in range(1,len(strs)):
                if strs[i-1][j] != strs[i][j]:
                    return public_str
                
            public_str += strs[0][j]
        return public_str

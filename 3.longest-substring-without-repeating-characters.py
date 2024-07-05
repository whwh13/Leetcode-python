class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        hash_table = {}
        t=0  # 当前行动中的子串长
        m=0  # 最长的子串长
        q=0  # 哈希表中最近一次截断

        for ii in range(0,l):
            char=s[ii]
            if char in hash_table and hash_table[char]>=q:
                    m=max(t,m)
                    q=hash_table[char]
                    t=ii-q
                    hash_table[char]=ii
                    
            else:
                t=t+1
                hash_table[char]=ii




        return max(m,t)

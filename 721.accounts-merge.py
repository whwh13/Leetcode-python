# 部分语法参考chatgpt，运算速度有点慢
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ii=0
        while ii < len(accounts):
            delete=False
            for jj in range(ii+1,len(accounts)):   
                if accounts[ii][0] == accounts[jj][0]:     # 如果用户名相同
                    if any(email in accounts[jj][1:] for email in accounts[ii][1:]):  # 如果有相同的邮箱
                        accounts[jj]=accounts[jj]+accounts[ii][1:]
                        accounts=accounts[:ii]+accounts[ii+1:]
                        delete=True
                        break

                                 
            if not delete:
                accounts[ii]= [accounts[ii][0]]+sorted(set(accounts[ii][1:]))
                ii += 1
        return accounts
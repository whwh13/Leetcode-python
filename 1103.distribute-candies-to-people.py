from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:       
        k = num_people*(num_people+1)//2
        t=0
        while candies > k + t*num_people*num_people:
            candies -= k + t*num_people*num_people
            t += 1
        
#        ii*t+num_people*t*(t+1)//2
        share=[t+num_people*t*(t-1)//2]
        if candies>t*num_people+1:
            share[0] += t*num_people+1
            candies -= t*num_people+1
        else:
            share[0] += candies
            candies = 0

        for ii in range(2,num_people+1):
            share += [ii*t+num_people*t*(t-1)//2]
            if candies>t*num_people+ii:
                share[ii-1] += t*num_people+ii
                candies -= t*num_people+ii
            else:
                share[ii-1] += candies
                candies = 0
        return share
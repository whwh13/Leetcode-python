from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        max_row=[max(grid[i]) for i in range(n)]
        max_col=[max(row[i] for row in grid) for i in range(n)]
        k=0
        for ii in range(n):
            for jj in range(n):
                max_num=min(max_row[ii],max_col[jj])
                k += max_num-grid[ii][jj]
        return k

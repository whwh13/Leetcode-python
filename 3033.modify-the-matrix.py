from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # m=len(matrix)
        # n=len(matrix[0])
        for jj in range(len(matrix[0])):
            rowNow=[row[jj] for row in matrix]
            t = max(rowNow)
            for ii in range(len(matrix)):
                if rowNow[ii]==-1:
                    matrix[ii][jj]=t
        return matrix
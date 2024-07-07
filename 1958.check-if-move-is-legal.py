from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        direction=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        if color=="W":
            icolor="B"
        else:
            icolor="W"

        for dire in direction:
            jj=1
            while jj:
                rr=rMove+jj*dire[0]
                cc=cMove+jj*dire[1]
                if rr >=0 and rr < 8 and cc >= 0 and cc < 8:
                    if board[rr][cc]==icolor:
                        jj=jj+1
                    elif board[rr][cc]==color:
                        if jj==1:
                            break
                        else:
                            return True
                    else:
                        break
                else:
                    break
        return False


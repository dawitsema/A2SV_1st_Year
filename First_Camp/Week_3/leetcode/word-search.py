from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        def helper(rw, cl, lenn):
            if lenn == len(word):
                return True

            if rw < 0 or cl < 0 or rw >= row or cl >= col or word[lenn] != board[rw][cl]:
                return False

            # Mark the current cell as visited
            temp = board[rw][cl]
            board[rw][cl] = "#"

            # Explore neighbors
            res = (helper(rw + 1, cl, lenn + 1) or helper(rw - 1, cl, lenn + 1) or
                   helper(rw, cl + 1, lenn + 1) or helper(rw, cl - 1, lenn + 1))

            # Restore the original value in the board
            board[rw][cl] = temp

            return res

        for i in range(row):
            for j in range(col):
                if helper(i, j, 0):
                    return True

        return False

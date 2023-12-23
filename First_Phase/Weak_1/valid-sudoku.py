class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        for i in range(9):
            for j in range(9):
                if board[i][j] in row:
                   print(board[i][j], row)
                   return False
                elif  board[i][j]!='.':
                    row.add(board[i][j])
            row.clear()
        row.clear()

        for i in range(9):
            for j in range(9):
                if board[j][i] in row:
                   print(board[j][i], row)
                   return False
                elif board[j][i] != '.' :
                    row.add(board[j][i])
            row.clear()
        subbox=[]

        for i in range(3):
            for j in range(3):
                for x in range(3):
                    for y in range(3):
                        if  board[x+i*3][y+j*3] in subbox:
                            return False
                            pass
                        elif  board[x+i*3][y+j*3]!=".":
                            subbox.append(board[x+i*3][y+j*3])
                subbox.clear()                

        return True
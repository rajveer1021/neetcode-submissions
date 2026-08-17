class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        for i in range(0, 9):
            for j in range(0,9):
                if board[i][j] in row:
                    return False
                else :
                    if board[i][j] == ".":
                        continue
                    row.add(board[i][j])
            row = set()

        column = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[j][i] in column:
                    return False
                else:
                    if board[j][i] == ".":
                        continue
                    column.add(board[j][i])
            column = set()


        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                matrix = set()
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j] in matrix:
                            return False
                        else:
                            if board[i][j] == ".":
                                continue
                            matrix.add(board[i][j])
                            
        return True
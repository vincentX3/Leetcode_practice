class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        record = [[0] * 9 for _ in range(27)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  # have number
                    num = int(board[i][j]) - 1
                    part = (i // 3) * 3 + j // 3
                    if record[i][num] != 0 or record[9 + j][num] != 0 or record[18 + part][num] != 0:
                        return False
                    else:
                        record[i][num], record[9 + j][num], record[18 + part][num] = 1, 1, 1

        return True
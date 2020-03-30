from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row, first_col = False, False
        # find zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        first_row = True
                    if j == 0:
                        first_col = True
                    matrix[0][j], matrix[i][0] = 0, 0  # mark the row, col
        # set zeros
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    # check first row, col
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return

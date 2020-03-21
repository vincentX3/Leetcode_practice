class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # v1 2 steps swap.
        if not matrix or len(matrix) < 2:
            return
        # step 1 , mirror-swap
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
        print(matrix)
        # step 2 , diagonal-swap
        for i in range(n - 1):
            for j in range(n - i):
                matrix[i][j], matrix[n - j - 1][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]

        return


if __name__ == '__main__':
    s = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(m)
    print(m)

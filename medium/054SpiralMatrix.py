from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        n, m = len(matrix), len(matrix[0])
        flag, i, j = 0, 0, 0  # control direction
        border = [m - 1, n - 1, 0, 1]
        ans = []
        count, total = 0, n * m
        while count < total:
            ans.append(matrix[i][j])
            count += 1
            if flag == 0:  # turn right
                if j < border[flag]:
                    j += 1
                else:
                    # reach border
                    border[flag] -= 1
                    flag += 1
                    i += 1
            elif flag == 1:  # turn down
                if i < border[flag]:
                    i += 1
                else:
                    border[flag] -= 1
                    flag += 1
                    j -= 1
            elif flag == 2:  # turn left
                if j > border[flag]:
                    j -= 1
                else:
                    border[flag] += 1
                    flag += 1
                    i -= 1
            else:  # turn up
                if i > border[flag]:
                    i -= 1
                else:
                    border[flag] += 1
                    flag = 0
                    j += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(s.spiralOrder(m2))

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        self.n, self.m = len(board), len(board[0])
        self.visited = [[0] * self.m for _ in range(self.n)]
        found = False
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:
                    found = self.find_word(board, word, i, j, 0)
                if found:
                    return True
        return False

    def find_word(self, board, word, i, j, idx):
        print(i, j, word[idx])
        if board[i][j] != word[idx]:
            return False
        else:
            if idx == len(word) - 1:
                return True  # found the word
            # mark visited
            self.visited[i][j] = 1
            # travel neighbours
            if i - 1 >= 0 and self.visited[i - 1][j] == 0:
                if self.find_word(board, word, i - 1, j, idx + 1):
                    return True
            if j - 1 >= 0 and self.visited[i][j - 1] == 0:
                if self.find_word(board, word, i, j - 1, idx + 1):
                    return True
            if i + 1 < self.n and self.visited[i + 1][j] == 0:
                if self.find_word(board, word, i + 1, j, idx + 1):
                    return True
            if j + 1 < self.m and self.visited[i][j + 1] == 0:
                if self.find_word(board, word, i, j + 1, idx + 1):
                    return True
            # remove mark
            self.visited[i][j] = 0
            return False


if __name__ == '__main__':
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(s.exist(board, word))

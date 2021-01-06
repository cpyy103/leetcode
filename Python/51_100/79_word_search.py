from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        len_word = len(word)
        visit = [[False] * n for i in range(m)]

        def dfs(i, j, k):
            if k == len_word:
                return True

            if i >= m or i < 0 or j >= n or j < 0 or board[i][j] != word[k]:
                return False
            if not visit[i][j] and board[i][j] == word[k]:
                visit[i][j] = True
                if dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1):
                    return True
                visit[i][j] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCCED'
    print(Solution().exist(board, word))

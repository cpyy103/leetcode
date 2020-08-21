from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or y < 0 or y >= m or x >= n or board[x][y] != 'O':
                return

            board[x][y] = 'A'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # 扫描边界，使用DFS
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        for i in range(1, m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]

    Solution().solve(board)
    for i in board:
        print(i)

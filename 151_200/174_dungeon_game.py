from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])

        for i in range(n - 2, -1, -1):
            dp[m - 1][i] = max(1, dp[m - 1][i + 1] - dungeon[m - 1][i])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j])

        return dp[0][0]


if __name__ == '__main__':
    dungeon = [[-2, -3, 3],
               [-5, -10, 1],
               [10, 30, -5]]
    print(Solution().calculateMinimumHP(dungeon))

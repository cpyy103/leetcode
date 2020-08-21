import math


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        dp = [0 for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * max(i - j, dp[i - j]))

        return dp[n]


class Solution1:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        elif b == 1:
            return int(math.pow(3, a - 1) * 4)
        elif b == 2:
            return int(math.pow(3, a) * 2)


if __name__ == "__main__":
    print(Solution().integerBreak(2))
    print(Solution().integerBreak(10))

    print(Solution1().integerBreak(2))
    print(Solution1().integerBreak(10))

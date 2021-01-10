from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[[0] * 2 for i in range(3)] for j in range(len(prices))]
        for i in range(3):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(3):
                if j == 0:
                    dp[i][j][0] = dp[i - 1][j][0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j][0] - prices[i])

        return max(dp[-1][0][0], dp[-1][1][0], dp[-1][2][0])


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        first_buy = -prices[0]
        first_sell = 0
        second_buy = -prices[0]
        second_sell = 0
        for price in prices:
            first_buy = max(first_buy, -price)
            first_sell = max(first_sell, first_buy + price)
            second_buy = max(second_buy, first_sell - price)
            second_sell = max(second_sell, second_buy + price)

        return second_sell


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    print(Solution().maxProfit(prices))
    print(Solution1().maxProfit(prices))

from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(left, right):
            if left == right:
                return nums[left]
            # 选择左边或右边中较大的一个
            return max(nums[left] - dfs(left + 1, right), nums[right] - dfs(left, right - 1))

        return dfs(0, n - 1) >= 0


class Solution1:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for i in range(n)]
        # 当i=j时，只能选择一个数据，没有多余的数可以选
        for i in range(n):
            dp[i][i] = nums[i]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0


class Solution2:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0 for i in range(n)]
        for i in range(n - 2, -1, -1):
            dp[i] = nums[i]
            data = dp[i]
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - data)
                data = dp[j]
        return dp[n - 1] >= 0


if __name__ == '__main__':
    # nums = [1, 5, 2]
    nums = [1, 5, 233, 7]
    print(Solution().PredictTheWinner(nums))
    print(Solution1().PredictTheWinner(nums))
    print(Solution2().PredictTheWinner(nums))

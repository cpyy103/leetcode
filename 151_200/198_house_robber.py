from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0 for _ in range(size)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, size):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[size - 1]


class Solution1:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for n in nums:
            cur, pre = max(pre + n, cur), cur

        return cur


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    print(Solution().rob(nums))

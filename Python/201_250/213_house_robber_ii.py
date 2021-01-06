from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.my_rob(nums[1:]), self.my_rob(nums[:-1]))

    def my_rob(self, nums):
        cur, pre = 0, 0
        for n in nums:
            cur, pre = max(pre + n, cur), cur

        return cur


if __name__ == '__main__':
    nums = [2, 3, 2]
    print(Solution().rob(nums))

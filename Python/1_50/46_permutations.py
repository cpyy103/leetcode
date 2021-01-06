from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], temp + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))

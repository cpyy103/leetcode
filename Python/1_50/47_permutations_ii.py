from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(nums, temp):
            if not nums:
                res.append(temp)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[:i] + nums[i + 1:], temp + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))


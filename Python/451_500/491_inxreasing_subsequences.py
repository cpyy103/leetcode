from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, temp):
            # 去重
            if len(temp) > 1 and temp not in res:
                res.append(temp)

            for i in range(len(nums)):
                # 控制递增
                if not temp or nums[i] >= temp[-1]:
                    dfs(nums[i + 1:], temp + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    print(Solution().findSubsequences(nums))

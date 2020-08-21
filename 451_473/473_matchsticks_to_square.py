from typing import List


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums or sum(nums) % 4 != 0:
            return False
        side = sum(nums) // 4  # 边长
        n = len(nums)

        nums.sort(reverse=True)  # 从大到小排，按顺序分
        sides = [0 for i in range(4)]

        def dfs(index):
            # 如果将所有的火柴分完，且各长度都等于目标边长，返回True
            if index == n:
                return sides[0] == sides[1] == sides[2] == sides[3] == side

            for i in range(4):
                if sides[i] + nums[index] <= side:
                    sides[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    sides[i] -= nums[index]
            return False

        return dfs(0)


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 2]
    print(Solution().makesquare(nums))

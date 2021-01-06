from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = 1
        max_res = nums[0]

        for n in nums:
            temp *= n
            max_res = max(max_res, temp)
            if n == 0:
                temp = 1

        temp = 1
        for n in nums[::-1]:
            temp *= n
            max_res = max(max_res, temp)
            if n == 0:
                temp = 1

        return max_res


if __name__ == '__main__':
    # nums = [2, 3, -2, 4]
    nums = [1, -2, 3, -4, 5, -6, 7]
    print(Solution().maxProduct(nums))

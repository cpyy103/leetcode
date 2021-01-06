from typing import List
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        for k, v in dic.items():
            if v == 1:
                return k


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == '__main__':
    nums = [2, 2, 1]
    print(Solution().singleNumber(nums))
    print(Solution1().singleNumber(nums))

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        n = len(nums)
        while i < n:
            start = i
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = i
            i += 1

            if start < end:
                res.append("{}->{}".format(nums[start], nums[end]))
            else:
                res.append(str(nums[start]))

        return res


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print(Solution().summaryRanges(nums))

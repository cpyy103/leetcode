from typing import List


class Solution:
    def __init__(self):
        self.temp = []
        self.res = 0

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        self.temp = [0 for _ in range(n)]
        self.merge_sort(nums, 0, n-1)
        return self.res
pass
    def merge_sort(self, nums, left, right):
        if left == right:
            return
        mid = (left + right) // 2

        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)

        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        print(left, right)
        for i in range(left, right + 1):
            self.temp[i] = nums[i]

        i = left
        j = mid + 1
        for k in range(left, right + 1):

            if i > mid:
                nums[k] = self.temp[j]
                j += 1
            elif j > right:
                nums[k] = self.temp[i]
                i += 1
            elif self.temp[i] <= self.temp[j]:
                nums[k] = self.temp[i]
                i += 1
            else:
                nums[k] = self.temp[j]
                j += 1
                self.res += (mid - i + 1)


if __name__ == "__main__":
    nums = [7, 5, 6, 4]
    print(Solution().reversePairs(nums))

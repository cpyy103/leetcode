from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        pre_sum = [0 for _ in range(n + 1)]
        for i in range(n):
            pre_sum[i + 1] = nums[i] + pre_sum[i]

        return self.merge(pre_sum, lower, upper, 0, n)

    def merge(self, pre_sum, lower, upper, left, right):
        if left == right:
            return 0
        mid = (left + right) // 2
        n1 = self.merge(pre_sum, lower, upper, left, mid)
        n2 = self.merge(pre_sum, lower, upper, mid + 1, right)
        res = n1 + n2

        i = left
        j_begin = mid + 1
        j_end = mid + 1
        while i <= mid:
            while j_begin <= right and pre_sum[j_begin] - pre_sum[i] < lower: j_begin += 1
            while j_end <= right and pre_sum[j_end] - pre_sum[i] <= upper: j_end += 1
            res += j_end - j_begin
            i += 1

        sort = [0 for _ in range(right - left + 1)]
        p1 = left
        p2 = mid + 1
        p = 0
        while p1 <= mid or p2 <= right:
            if p1 > mid:
                sort[p] = pre_sum[p2]
                p2 += 1
            elif p2 > right:
                sort[p] = pre_sum[p1]
                p1 += 1
            else:
                if pre_sum[p1] < pre_sum[p2]:
                    sort[p] = pre_sum[p1]
                    p1 += 1
                else:
                    sort[p] = pre_sum[p2]
                    p2 += 1
            p += 1

        for j in range(len(sort)):
            pre_sum[left + j] = sort[j]

        return res


if __name__ == '__main__':
    nums = [2, -1, 4, 3, -4, 2, -1, 1]
    lower = -2
    upper = 2
    print(Solution().countRangeSum(nums, lower, upper))

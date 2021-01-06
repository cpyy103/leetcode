from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  # 确保nums1短
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        if m == 0:
            return (nums2[n // 2] + nums2[(n - 1) // 2]) / 2

        size = m + n
        cutL, cutR = 0, m
        cut1 = m // 2
        cut2 = size // 2 - cut1
        min_value = -2 ** 31
        max_value = 2 ** 31

        while True:
            cut1 = (cutR - cutL) // 2 + cutL
            cut2 = size // 2 - cut1

            # 解决边界问题
            left_1 = nums1[cut1 - 1] if cut1 != 0 else min_value
            left_2 = nums2[cut2 - 1] if cut2 != 0 else min_value
            right_1 = nums1[cut1] if cut1 != m else max_value
            right_2 = nums2[cut2] if cut2 != n else max_value

            if left_1 > right_2:
                cutR = cut1 - 1
            elif left_2 > right_1:
                cutL = cut1 + 1
            else:
                if size % 2 == 0:
                    left = left_1 if left_1 > left_2 else left_2
                    right = right_1 if right_1 < right_2 else right_2
                    return (left + right) / 2
                else:
                    return right_1 if right_1 < right_2 else right_2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [3, 5, 8, 9]
    nums2 = [1, 2, 7, 10, 11, 12]
    print(Solution().findMedianSortedArrays(nums1, nums2))

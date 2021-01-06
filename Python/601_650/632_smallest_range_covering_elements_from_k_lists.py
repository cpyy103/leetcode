from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        # 用于保存该区间中的k个列表中的某个元素
        k_elements = [nums[i][0] for i in range(k)]

        # 用于保存这k个数在各自列表中的下标
        indices = [0 for _ in range(k)]
        # 初始区间为k个元素的最小值到最大值
        start = left = min(k_elements)
        end = right = max(k_elements)
        length = end - start

        while True:
            # 获取最小值所在的数组的下标
            index = k_elements.index(left)
            # 如果该最小值为所在数组的最后一个值，退出
            if indices[index] == len(nums[index]) - 1:
                break
            # 该最小值所在数组的位置后移一个位置
            # 将后一个数据更新到k_elements中
            indices[index] += 1
            k_elements[index] = nums[index][indices[index]]
            # 如果更新后的数大于右端，则更新右段指针
            if k_elements[index] > right:
                right = k_elements[index]
            # 更新最小值
            left = min(k_elements)
            # 更新区间
            if right - left < length:
                start = left
                end = right
                length = right - left

        return [start, end]


if __name__ == '__main__':
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    print(Solution().smallestRange(nums))

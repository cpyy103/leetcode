from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后往前寻找第一次出现正序的位置，k为出现的正序两个数字中前一个数字的下标
        k = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                k = i - 1
                break

        # 数字全为逆序，当前值为最大值，直接逆序变为最小值
        if k == -1:
            nums.reverse()
            return

        # 将后面k个数逆序
        nums[k + 1:] = nums[:k:-1]
        # 交换
        # 由于后面的数已经是正序，第一个大于nums[k]的数就是合适的数
        for i in range(k + 1, len(nums)):
            if nums[k] < nums[i]:
                nums[k], nums[i] = nums[i], nums[k]
                break


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(nums)

    Solution().nextPermutation(nums)
    print(nums)

    Solution().nextPermutation(nums)
    print(nums)

    Solution().nextPermutation(nums)
    print(nums)

    Solution().nextPermutation(nums)
    print(nums)

    Solution().nextPermutation(nums)
    print(nums)

from typing import List


# 超时
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_dic = {}

        longest_length = 0

        for num in nums:
            # 如果其前一个数存在于字典中
            if num - 1 in nums_dic:
                nums_dic[num] = nums_dic[num - 1] + 1
            else:
                nums_dic[num] = 1
            # 判断这个数后面的连续的数是否存在于数组中
            while num + 1 in nums_set:
                nums_dic[num + 1] = nums_dic[num] + 1
                num += 1

            longest_length = max(longest_length, nums_dic[num])

        return longest_length


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0

        for num in nums:
            if num - 1 not in nums_set:
                cur = 1  # 用于计算当前连续序列的长度
                while num + 1 in nums_set:
                    num += 1
                    cur += 1
                longest_length = max(longest_length, cur)

        return longest_length


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))
    print(Solution1().longestConsecutive(nums))

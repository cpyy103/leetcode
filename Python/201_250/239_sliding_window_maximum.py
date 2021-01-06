from typing import List
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)

        res = [-heap[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            # 判断堆顶是否存在于滑动窗口中
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])

        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))
    print(Solution1().maxSlidingWindow(nums, k))

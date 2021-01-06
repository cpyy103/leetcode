from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            left = right = i
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right < n and heights[right] >= heights[i]:
                right += 1

            max_area = max(max_area, heights[i] * (right - left - 1))
        return max_area


class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights.append(0)
        n = len(heights)
        stack = [-1]
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                max_area = max(max_area, heights[top] * (i - stack[-1] - 1))
            stack.append(i)

        return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(Solution().largestRectangleArea(heights))
    print(Solution1().largestRectangleArea(heights))

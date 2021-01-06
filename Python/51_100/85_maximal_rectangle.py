from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            max_area = 0
            heights.append(0)
            n = len(heights)
            stack = [-1]
            for i in range(n):
                while len(stack) > 1 and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    max_area = max(max_area, heights[top] * (i - stack[-1] - 1))
                stack.append(i)

            return max_area

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        max_area = 0
        dp = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(dp))

        return max_area


if __name__ == '__main__':
    maxtrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(Solution().maximalRectangle(maxtrix))

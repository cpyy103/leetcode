"""
118.杨辉三角 https://leetcode-cn.com/problems/pascals-triangle/
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        triangle = [[1], [1, 1]]

        for i in range(2, numRows):
            temp = [1 for _ in range(i+1)]

            for j in range(1, len(temp)-1):
                temp[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(temp)

        return triangle


if __name__ == '__main__':
    num = 4
    solution = Solution()
    print(solution.generate(num))

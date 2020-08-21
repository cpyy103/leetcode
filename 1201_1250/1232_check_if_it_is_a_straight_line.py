from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        delta_y = (coordinates[1][1] - coordinates[0][1])
        delta_x = (coordinates[1][0] - coordinates[0][0])
        for i in range(2, len(coordinates)):
            delta_y_ = coordinates[i][1] - coordinates[0][1]
            delta_x_ = coordinates[i][0] - coordinates[0][0]
            if delta_y * delta_x_ != delta_y_ * delta_x:
                return False

        return True


if __name__ == '__main__':
    coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
    print(Solution().checkStraightLine(coordinates))

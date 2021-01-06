from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        result = []
        for interval in intervals[1:]:
            # 当前区间存在重叠，当前区间起始位置小于上一区间的结束位置
            if interval[0] <= end:
                end = max(end, interval[1])
            # 当前不存在重叠
            else:
                result.append([start, end])  # 加入解集
                start = interval[0]  # 更新start end
                end = interval[1]

        result.append([start, end])

        return result


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))

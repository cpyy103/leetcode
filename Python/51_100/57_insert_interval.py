from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def merge(intervals):
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

        intervals.append(newInterval)
        return merge(intervals)


class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        if n == 0:
            return [newInterval]

        while i < n and newInterval[0] > intervals[i][1]:
            i += 1
        left = i
        while i < n and newInterval[1] >= intervals[i][0]:
            i += 1
        right = i
        
        if left >= n:
            result = intervals + [newInterval]
        elif left == right:
            intervals.insert(left, newInterval)
            result = intervals
        else:
            result = intervals[:left] + \
                     [[min(intervals[left][0], newInterval[0]), max(intervals[right - 1][1], newInterval[1])]] + \
                     intervals[right:]
        return result


if __name__ == '__main__':
    interval = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(interval, newInterval))
    print(Solution1().insert(interval, newInterval))

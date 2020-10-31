from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: (x[0], x[1]))

        if clips[-1][1] < T:
            return -1

        res = 1
        start = 0
        end = 0  # 当前所能到达的最远位置

        for i in range(len(clips)):
            # 如果当前片段的起始大于最远位置，出现了空白
            if clips[i][0] > end:
                return -1
            # 更新
            elif clips[i][0] > start:
                start = end
                res += 1

            end = max(end, clips[i][1])

            if clips[i][1] >= T:
                break

        return res


if __name__ == '__main__':
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    T = 10
    print(Solution().videoStitching(clips, T))

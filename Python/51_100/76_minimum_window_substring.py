from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1

        t_len = len(t)
        left = 0
        min_left = 0
        min_right = len(s)

        for right, char in enumerate(s):  # 这样写的话每次窗口右端right自动右移
            if char in t_dict and t_dict[char] > 0:
                t_len -= 1

            if char in t_dict:
                t_dict[char] -= 1

            # 窗口中已包含所有字符，需要移动left找到最短窗口
            if t_len == 0:
                while True:
                    if s[left] not in t_dict:  # 跳过非t中的字符
                        left += 1
                    elif t_dict[s[left]] < 0:  # 跳过比t出现中更多次的多余字符
                        t_dict[s[left]] += 1
                        left += 1
                    else:
                        break

                # 最小窗口
                if right - left < min_right - min_left:
                    min_left, min_right = left, right
                # 最小窗口的第一个字符肯定是t中的字符，left向后滑动
                t_dict[s[left]] += 1
                t_len += 1
                left += 1

        # 如果min_right没有发生变化，说明没有最小窗口，也就是无解
        return '' if min_right == len(s) else s[min_left:min_right + 1]


if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    print(Solution().minWindow(S, T))

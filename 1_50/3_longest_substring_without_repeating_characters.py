class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = -1  # 初始位置长度，用于记录上一个重复字符的位置
        res = 0
        for right in range(len(s)):
            # 当出现重复元素时，更新left
            if s[right] in dic:
                left = max(dic[s[right]], left)
            res = max(res, right - left)
            dic[s[right]] = right  # 添加/更新字符位置

        return res


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        res = 0  # 保存最大的长度
        cur = 0  # 当前窗口的长度
        for right in range(len(s)):
            cur += 1
            # 从左往右删除元素，直到窗口中没有重复字符
            while s[right] in window:
                window.remove(s[left])
                left += 1
                cur -= 1
            res = max(res, cur)
            window.add(s[right])
        return res


if __name__ == '__main__':
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
    print(Solution1().lengthOfLongestSubstring(s))

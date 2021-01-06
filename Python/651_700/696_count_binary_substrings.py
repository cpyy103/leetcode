class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        last = ''
        cur = 0     # 记录当前字符的数量
        pre = 0     # 记录上一个不同字符的数量
        for c in s:
            if c == last:
                cur += 1
            else:
                last = c
                res += min(cur, pre)
                pre, cur = cur, 1

        return res + min(cur, pre)


if __name__ == '__main__':
    s = '11001100'
    # s = '10101'
    print(Solution().countBinarySubstrings(s))

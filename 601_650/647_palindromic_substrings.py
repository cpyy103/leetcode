class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        ss = '#' + '#'.join(list(s)) + '#'
        n = len(ss)
        for i in range(n):
            left = right = i
            while left > 0 and right < n - 1 and ss[left] == ss[right]:
                if ss[left] != '#':
                    res += 1
                left -= 1
                right += 1

        return res


class Solution1:
    def __init__(self):
        self.res = 0
        self.s = None
        self.n = None

    def countSubstrings(self, s: str) -> int:
        self.s = s
        self.n = len(s)
        for i in range(self.n):
            self.is_palindromic(i, i)
            self.is_palindromic(i, i + 1)
        return self.res

    def is_palindromic(self, left, right):
        while left >= 0 and right <= self.n - 1 and self.s[left] == self.s[right]:
            self.res += 1
            left -= 1
            right += 1


class Solution2:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = 1
                    res += 1

        return res


if __name__ == '__main__':
    s = 'aaa'
    print(Solution().countSubstrings(s))
    print(Solution1().countSubstrings(s))
    print(Solution2().countSubstrings(s))

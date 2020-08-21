class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == None or p == None:
            return False
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        dp[0][0] = True  # dp[i][j]表示s的前i个元素能否被p的前j个匹配
        for i in range(len(p)):
            if p[i] == '*' and dp[0][i - 1]:
                dp[0][i + 1] = True

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] == s[i] or p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = (dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1])

                        # dp[i][j] = dp[i-1][j] // 多个字符匹配的情况
                        # or dp[i][j] = dp[i][j-1] // 单个字符匹配的情况
                        # or dp[i][j] = dp[i][j-2] // 没有匹配的情况

        return dp[len(s)][len(p)]


if __name__ == '__main__':
    s = 'aa'
    p = 'a'
    print(Solution().isMatch(s, p))

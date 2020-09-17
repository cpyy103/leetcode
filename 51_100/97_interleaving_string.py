class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if (len1 + len2) != len3:
            return False
        dp = [[False for i in range(len2 + 1)] for j in range(len1 + 1)]
        # 初始化
        dp[0][0] = True

        for i in range(1, len1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = True
            else:
                break
        for j in range(1, len2 + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = True
            else:
                break

        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = (dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1])) or (dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1]))

        return dp[len1][len2]


if __name__ == '__main__':
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'
    print(Solution().isInterleave(s1, s2, s3))

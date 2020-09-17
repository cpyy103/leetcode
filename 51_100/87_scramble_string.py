class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)
        # s1 s2 字符串长度需相同
        if len1 != len2:
            return False
        # 最里面的长度为len1+1，用不到dp[i][j][0]
        dp = [[[False for _ in range(len1 + 1)] for _ in range(len1)] for _ in range(len1)]

        # 初始化
        for i in range(len1):
            for j in range(len1):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True

        # 各区间长度，长度为1的单字符已经初始化了，长度最大为原始字符串的长度
        for k in range(2, len1 + 1):
            # i的初始位置为0，最后的位置肯定要与len1差k个
            # 不然从i到len1就不足k的长度了
            for i in range(len1 - k + 1):
                # j也一样
                for j in range(len1 - k + 1):
                    # 长度为k的字符串再分割出子串，w为分割线
                    for w in range(1, k):
                        # 第一种情况
                        if dp[i][j][w] and dp[i + w][j + w][k - w]:
                            dp[i][j][k] = True
                            # 满足条件就直接break，表示可以变换，直接进行行下一循环
                            break
                        # 第二种情况
                        if dp[i][j + k - w][w] and dp[i + w][j][k - w]:
                            dp[i][j][k] = True
                            break

        return dp[0][0][len1]


class Solution1:
    def isScramble(self, s1: str, s2: str) -> bool:
        # 如果两个字串相同
        if s1 == s2:
            return True
        # 两个子串包含不同的字符
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            # 第一种情况
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            # 第二种情况
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


if __name__ == '__main__':
    s1 = 'great'
    s2 = 'rgeta'
    print(Solution().isScramble(s1, s2))
    print(Solution1().isScramble(s1, s2))

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.dfs(s, [])
        return self.res

    def is_valid(self, section):
        if section and str(int(section)) == section and 0 <= int(section) <= 255:
            return True
        else:
            return False

    def dfs(self, s, temp):
        # s为当前所需要检索的字符串
        # temp为已经正确解析出的地址段
        # 如果s已经全部取完，且temp里已存在4段地址，说明已经解析一条正确地址
        if len(s) == 0 and len(temp) == 4:
            self.res.append('.'.join(temp))
        if len(temp) < 4:
            # 一个section的最大长度为3
            # 如果最后的剩下的s长度小于3，则到s长度为止
            for i in range(min(3, len(s))):
                section = s[:i + 1]
                if self.is_valid(section):
                    self.dfs(s[i + 1:], temp + [section])


if __name__ == '__main__':
    s = '25525511135'
    print(Solution().restoreIpAddresses(s))

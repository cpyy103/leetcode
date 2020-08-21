from collections import defaultdict
from typing import List


class Solution(object):
    def __init__(self):
        self.res = []
        self.dic = defaultdict(set)  # 保存同种模式下的单词信息
        self.length = 0  # 每个单词长度
        self.word_level = {}  # 记录各单词节点层数
        self.i = 0

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.dic[word[:i] + "*" + word[i + 1:]].add(word)

        self.bfs(beginWord)
        self.dfs(beginWord, endWord, [beginWord])

        return self.res

    # 记录单词层数
    def bfs(self, beginWord):
        self.word_level[beginWord] = 0
        queue = [beginWord]
        while queue:
            cur = queue.pop(0)
            for word in self.get_next_words(cur):
                if word not in self.word_level:
                    self.word_level[word] = self.word_level[cur] + 1
                    queue.append(word)

    # 回溯查找
    def dfs(self, cur, target, temp):
        if cur == target:
            self.res.append(temp[:])
            return

        for word in self.get_next_words(cur):
            # 如果当前单词cur的下一层不包含该邻居节点word，直接跳过
            # 由于没有设置visit集合来标记是否已经遍历过，word可能为cur上一层节点
            if self.word_level[cur] + 1 != self.word_level[word]:
                continue

            temp.append(word)
            self.dfs(word, target, temp)
            temp.pop()

    # 获取邻居节点
    def get_next_words(self, cur):
        words = []
        for i in range(self.length):
            for word in self.dic[cur[:i] + "*" + cur[i + 1:]]:
                words.append(word)

        return words


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(Solution().findLadders(beginWord, endWord, wordList))

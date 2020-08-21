from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        length = len(beginWord)

        dic = defaultdict(set)

        for word in wordList:
            for i in range(length):
                dic[word[:i] + "*" + word[i + 1:]].add(word)

        word_level = {beginWord: 0}
        queue = [beginWord]
        while queue:
            cur = queue.pop(0)
            for i in range(length):
                for word in dic[cur[:i] + "*" + cur[i + 1:]]:
                    if word not in word_level:
                        word_level[word] = word_level[cur] + 1
                        queue.append(word)

                    if word == endWord:
                        return word_level[word] + 1

        return 0


class Solution1(object):
    def __init__(self):
        self.length = 0
        self.dic = defaultdict(set)

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        self.length = len(beginWord)
        for word in wordList:
            for i in range(self.length):
                self.dic[word[:i] + "*" + word[i + 1:]].add(word)

        queue_begin = [(beginWord, 1)]
        queue_end = [(endWord, 1)]
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        while queue_begin and queue_end:
            ans = self.visit(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            ans = self.visit(queue_end, visited_end, visited_begin)
            if ans:
                return ans
        return 0

    def visit(self, queue, visited, other_visited):
        cur, level = queue.pop(0)
        for i in range(self.length):
            pattern = cur[:i] + "*" + cur[i + 1:]
            for word in self.dic[pattern]:
                if word in other_visited:
                    return level + other_visited[word]
                if word not in visited:
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None


class Solution3:
    def __init__(self):
        self.length = 0
        self.dic = defaultdict(set)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                self.dic[word[:i] + "*" + word[i + 1:]].add(word)

        word_level_begin = {beginWord: 0}
        queue_begin = [beginWord]

        word_level_end = {endWord: 0}
        queue_end = [endWord]
        while queue_begin and queue_end:
            ans = self.visit(queue_begin, word_level_begin, word_level_end)
            if ans:
                return ans
            ans = self.visit(queue_end, word_level_end, word_level_begin)
            if ans:
                return ans

        return 0

    def visit(self, queue, word_level, other_word_level):
        cur = queue.pop(0)
        for i in range(self.length):
            for word in self.dic[cur[:i] + "*" + cur[i + 1:]]:
                if word not in word_level:
                    word_level[word] = word_level[cur] + 1
                    queue.append(word)
                if word in other_word_level:
                    return word_level[word] + other_word_level[word] + 1
        return None


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(Solution3().ladderLength(beginWord, endWord, wordList))

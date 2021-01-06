from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        ans = []
        word_dic = {}
        word_len = len(words[0])
        word_num = len(words)
        for word in words:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1
        for i in range(len(s) - word_len * word_num + 1):  # 当剩余字符串长度不足所有长度时即可退出循环
            count = 0
            j = i
            word_dic_copy = word_dic.copy()
            while count < word_num:
                cur = s[j:j + word_len]
                if cur in word_dic_copy and word_dic_copy[cur] != 0:
                    j += word_len
                    word_dic_copy[cur] -= 1
                    count += 1
                else:
                    break

            if count == word_num:
                ans.append(i)

        return ans


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(Solution().findSubstring(s, words))

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        length = [len(word) for word in words]
        n_words = len(words)
        i = 0  # 记录已使用的单词数
        result = []
        while i < n_words:  # 仍有为使用的单词
            temp = []  # 记录这一行中的单词
            temp_len = 0  # 已使用的长度，每次 一个单词加一个空格
            temp_n = 0  # 这一行中的单词数
            while True:
                # 如果加上下一个单词的长度不大于最大长度
                if i < n_words and temp_len + length[i] <= maxWidth:
                    temp.append(words[i])
                    temp_len += length[i] + 1  # 还要加一个空格
                    temp_n += 1
                    i += 1
                else:
                    break

            # 最后一行单词，左对齐
            if n_words == i:
                res = ' '.join(temp) + ' ' * (maxWidth - temp_len + 1)
                result.append(res)
                break

            # 不是最后一行的单词
            # 只有一个单词
            if temp_n == 1:
                result.append(temp[0] + ' ' * (maxWidth - len(temp[0])))
            # 两个单词
            elif temp_n == 2:
                result.append(temp[0] + ' ' * (maxWidth - len(temp[0]) - len(temp[1])) + temp[1])
            # 有3个及以上单词
            else:
                sum_word_len = sum([len(word) for word in temp])  # 实际单词总长度
                m = (maxWidth - sum_word_len) // (temp_n - 1)  # 平均每个空的长度，向下取整
                n = (maxWidth - sum_word_len) - m * (temp_n - 1)  # 多余的空
                res = temp[0]

                for j in range(1, temp_n):
                    if n > 0:
                        res += ' ' * (m + 1) + temp[j]
                        n -= 1
                    else:
                        res += ' ' * m + temp[j]
                result.append(res)

        return result


if __name__ == '__main__':
    words = ["Science", "is", "what", "we", "understand", "well",
             "enough", "to", "explain", "to", "a", "computer.", "Art",
             "is", "everything", "else", "we", "do"]
    maxWidth = 20

    res = Solution().fullJustify(words, maxWidth)
    for r in res:
        print(r)

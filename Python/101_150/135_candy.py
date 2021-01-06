from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        right = [1] * n
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        res = 0
        for i in range(n):
            res += max(left[i], right[i])

        return res


class Solution1:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # 从右往左时，最右边的孩子要么是1颗糖，要么是left[n-1]颗糖
        # 并且left[n-1] >= 1
        res = left[n - 1]
        right = 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right += 1
            else:
                right = 1
            res += max(left[i], right)

        return res


if __name__ == '__main__':
    rating = [1, 2, 4, 3, 2]
    print(Solution().candy(rating))
    print(Solution1().candy(rating))

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) != 0:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)

        return max_len


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for _ in range(n)]

        for i in range(1, n):
            if s[i] == ')':
                pre = i - dp[i - 1] - 1
                if pre >= 0 and s[pre] == '(':
                    dp[i] = dp[i - 1] + 2

                    if pre > 0:
                        dp[i] += dp[pre - 1]

        return max(dp)


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * left)
            elif right > left:
                left, right = 0, 0

        left, right = 0, 0

        for c in s[::-1]:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left, right = 0, 0

        return max_length


if __name__ == '__main__':
    s = '(()'
    print(Solution().longestValidParentheses(s))
    print(Solution1().longestValidParentheses(s))
    print(Solution2().longestValidParentheses(s))

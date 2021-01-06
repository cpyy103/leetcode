class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_pos = {}
        for i, c in enumerate(s):
            last_pos[c] = i

        print(last_pos)

        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while len(stack) > 0 and stack[-1] > c and last_pos[stack[-1]] > i:
                stack.pop()

            stack.append(c)

        return ''.join(stack)


if __name__ == '__main__':
    s = 'cbacdcbc'
    print(Solution().removeDuplicateLetters(s))

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))


class Solution1:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ''
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            temp = n1 + n2 + carry
            carry = temp // 10
            res = str(temp % 10) + res
            i -= 1
            j -= 1
        return '1' + res if carry else res


if __name__ == "__main__":
    num1 = "123"
    num2 = "789"
    print(Solution().addStrings(num1, num2))
    print(Solution1().addStrings(num1, num2))

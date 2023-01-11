# [Pow(x,n)](https://leetcode-cn.com/problems/powx-n/)

## 描述  
**中等**
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

**示例**

    输入: 2.00000, 10
    输出: 1024.00000
    
    输入: 2.10000, 3
    输出: 9.26100
    
    输入: 2.00000, -2
    输出: 0.25000
    解释: 2-2 = 1/22 = 1/4 = 0.25
    
    说明:
    -100.0 < x < 100.0
    n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

## 解题  
哈哈，这种题，我直接一个return解决战斗  
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)
```
en，这是是不是太坏了  

然后就撸了一个暴力的，一个个连乘，结果，超出了时间限制  

```python 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if x==0:
            return 0

        if n<0:
            x = 1/x
            n = -n

        ans = 1
        for i in range(n):
            ans *= x
        return ans

if __name__ == '__main__':
    # 就是这个例子，超出时间限制
    print(Solution().myPow(0.00001, 2147483647))
```
然后就换一种，我们都知道
$$
x^{2m}=(x^m)^2
$$
所以
$$
x^{n}=(x^{\frac{n}{2}})^2
$$
讨论n的奇偶性，如果n为**偶数**
$$
x^n=A*A
$$
如果n为**奇数**
$$
x^n=A*A*x
$$
可以用递归实现，被称为快速幂

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x, n):
            if n==0:
                return 1.0
            half = fastPow(x, n//2)
            print(half)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

        if n < 0:
            x = 1 / x
            n = -n

        return fastPow(x, n)
```


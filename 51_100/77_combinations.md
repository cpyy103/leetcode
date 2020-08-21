# [组合](https://leetcode-cn.com/problems/combinations/)

## 描述  
**中等** 
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

## 示例

    输入: n = 4, k = 2
    输出:
    [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]

## 解题  

一道简单的回溯问题  
只需判断回溯函数的k是否为0，即还需要k个数才能组成一个解  
i表示每个解中添加的数的范围
一开始写的时候，没有copy()，最后的结果为空，不知道原因  
后来发现，res结果append的是temp，而temp一直在变化，最后temp为空，所以res的每个解都为空  

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def back(k, temp, i):
            if k == 0:
                res.append(temp.copy())
                return 
            for j in range(i, n+1):
                temp.append(j)
                back(k-1, temp, j+1)
                temp.pop()

        back(k, [], 1)
        return res

```
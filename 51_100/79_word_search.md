# [单词搜索](https://leetcode-cn.com/problems/word-search/)

## 描述  
**中等** 
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

## 示例

    board =
    [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]

    给定 word = "ABCCED", 返回 true.
    给定 word = "SEE", 返回 true.
    给定 word = "ABCB", 返回 false.

## 解题 

深度优先遍历，回溯  
建立visit矩阵，如果已经把一点加入路径，则visit对应上的点为1

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k, visit):
            if k == len(word):
                return True
            if i>=m or i<0 or j>=n or j<0 or board[i][j]!=word[k]:
                return False
            if visit[i][j]==0 and board[i][j]==word[k]:
                visit[i][j] = 1

                if dfs(i+1, j, k+1, visit) or dfs(i-1, j, k+1, visit) or \
                    dfs(i, j+1, k+1, visit) or dfs(i, j-1, k+1, visit):
                    return True

                visit[i][j] = 0
                return False

        visit = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0, visit):
                    return True

        return False
```

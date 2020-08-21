# [最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

## 描述  
**困难**  
给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
 
## 示例

    输入:
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    输出: 6

## 解题  
[官方题解](https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/)挺好

首先将每行的数据转化一下  
例如[1,1,0,1,1,1,1]可以转为[1,2,0,1,2,3,4]    
表示一行内的最大面积  

然后将上面的例子转化为  

    [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 2, 3],
        [1, 2, 3, 4, 5],
        [1, 0, 0, 1, 0]
    ]

然后就可以按照第84题，将每一列看一组数  
例如 

    [1, 1, 1, 1]
    [0, 0, 2, 0]
    [1, 1, 3, 0]
    [0, 2, 4, 1]
    [0, 3, 5, 0]

找出每一组的最大矩形，然后再取最大  

部分代码直接从第84题复制过来

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            max_area = 0
            heights.append(0)
            n = len(heights)
            stack = [-1]
            for i in range(n):
                while len(stack)>1 and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    area = heights[top] * (i-stack[-1]-1)
                    max_area = max(max_area, area)
                stack.append(i)

            return max_area

        if len(matrix)==0 or len(matrix[0]) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        new_matrix = [[0 for i in range(n)] for j in range(m)]
        heights = []
        for j in range(n):
            temp = []
            for i in range(m):
                if matrix[i][j] == '1':
                    new_matrix[i][j] = 1 + (new_matrix[i][j-1] if j > 0 else 0)
                temp.append(new_matrix[i][j])
            heights.append(temp)

        max_area = 0
        for j in range(n):
            max_area = max(max_area, largestRectangleArea(heights[j]))
        
        return max_area

```
动态规划的官方题解，挺好

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea
```






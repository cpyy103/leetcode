# [不同的二叉搜索树II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/)

## 描述    
**中等**  
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

## 示例:

    输入: 3
    输出:
    [
      [1,null,3,2],
      [3,2,null,1],
      [3,1,null,null,2],
      [2,1,3],
      [1,null,2,null,3]
    ]
    解释: 
    以上的输出对应以下 5 种不同结构的二叉搜索树：

    1         3     3       2      1
      \       /     /      / \      \
       3     2     1      1   3      2
      /     /       \                 \
    2     1          2                 3

## 解题  
根节点为取值为[1,n]，设取i  
左儿子取值为[1,i-1]  
右儿子取值为[i+1,n]  
然后再生成左/右儿子的子树    

递归求左/右子树的所有排列  

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n<1:
            return []
        else:
            return self.generate(1, n)

    def generate(self, left, right):
        res = []
        if left>right:
            return None
        
        for i in range(left, right+1):
            # 所有左子树
            left_node = self.generate(left, i-1)
            # 所有右子树
            right_node = self.generate(i+1, right)
            # 组合所有方式
            for l in left_node:
                for r in right_node:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res



```


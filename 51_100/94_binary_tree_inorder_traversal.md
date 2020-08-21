# [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)


## 描述  
**中等**  
给定一个二叉树，返回它的中序 遍历。

## 示例

    输入: [1,null,2,3]
        1
          \
            2
          /
        3

    输出: [1,3,2]

## 解题  
数据结构的基本知识  
中序遍历，左子树->父节点（根节点）->右节点  

递归
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)
        return res

```
或者python一行递归  

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return [] if not root else self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

```

非递归  

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        p = root
        stack = []
        res = []
        while p or len(stack):
            if p:
                stack.append(p)
                p = p.left
            else:
                p = stack.pop()
                res.append(p.val)
                p = p.right

        return res
```






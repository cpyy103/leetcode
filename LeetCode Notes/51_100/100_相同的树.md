# [相同的树](https://leetcode-cn.com/problems/same-tree/)  

## 描述  
**中等**  

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例 1:**

    输入:     1         1
             / \       / \
            2   3     2   3
    
            [1,2,3],   [1,2,3]
    
    输出: true
**示例 2:**

    输入:      1        1
             /           \
            2             2
    
            [1,2],     [1,null,2]
    
    输出: false
**示例 3:**

    输入:    1         1
            / \       / \
           2   1     1   2
    
            [1,2,1],   [1,1,2]
    
    输出: false

## 解题  

递归   

按照顺序一个一个判断是否相等  

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

栈实现非递归中序遍历

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        stack_p = []
        stack_q = []

        while p or q or len(stack_p) > 0 or len(stack_q) > 0:
            if p and q:
                stack_p.append(p)
                stack_q.append(q)
                p = p.left
                q = q.left
            elif not p and not q:
                p = stack_p.pop()
                q = stack_q.pop()
                if p.val != q.val:
                    return False
                p = p.right
                q = q.right
            else:
                return False

        return True
        

```


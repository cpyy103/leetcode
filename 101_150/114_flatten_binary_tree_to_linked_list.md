# [二叉树展开为链表](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/)

## 描述  
**中等**  
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

        1
       / \
      2   5
     / \   \
    3   4   6
将其展开为：

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

## 解题  

展开的结果类似于将二叉树进行先序遍历然后按顺序挂在right指针上  

如果是遍历一个值挂在右边，容易丢弃原来的右子树   

所以设置一个栈，用来保存右子树 


```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        stack = []
        stack.append(root)
        pre = None
        while len(stack):
            temp = stack.pop()
            if pre:
                pre.right = temp
                pre.left = None
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            pre = temp
```







```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        p = root
        while p:
            # 左子树为空，考虑下一个节点
            if not p.left:
                p = p.right
            else:
                # 找到左子树最右边的节点
                q = p.left
                while q.right:
                    q = q.right
                # 将原右子树接到左子树最右边节点
                q.right = p.right
                # 将左子树接到当前节点右子树
                p.right = p.left
                # 设置当前左子树为None
                p.left = None
                # 下一个节点
                p = p.right
```






# [二叉树的层序遍历II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)

## 描述  
**简单**  
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

 
## 示例
二叉树：[3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
返回其层次遍历结果：

    [
        [15,7],
        [9,20],
        [3]
    ]

## 解题  
参考[第102题](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)，每次将temp列表插在res第一个位置  

queue中保存一层的节点  
当扫描queue中节点时，一直pop当前层的节点，然后加入下一层的节点  

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)

        while queue:
            temp = [] # 当前层的节点值
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            
            res.insert(0, temp)
        
        return res

```

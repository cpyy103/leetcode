# [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

## 描述  
中等 
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


**示例**
二叉树：[3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7

返回其层次遍历结果：

    [
        [3],
        [9,20],
        [15,7]
    ]

## 解题    
借助队列（列表）  
BFS   
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            temp = [] # temp为当前层节点值
            for i in range(len(queue)): 
                # 扫描这一层的节点
                # 然后将这一层的数值加入temp，并将各节点的孩子加入队列
                node = queue.pop(0) # 取出queue的第一个元素
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            res.append(temp)
        return res
```

DFS    
深度优先遍历，在解集的每一层解中依次加上节点值

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self.add_node(root, 0)
        return self.res
    
    def add_node(self, root, level):
        if not root:
            return  
        # 新的一层，增加该层的解
        if len(self.res) == level:
            self.res.append([])
        # 在对应的层加入节点值
        self.res[level].append(root.val)
        # 将该节点的左右孩子加入下一层
        self.add_node(root.left, level+1)
        self.add_node(root.right, level+1) 
```

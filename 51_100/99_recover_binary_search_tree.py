# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class createTree:
    def create(self, nodes):
        root = TreeNode(nodes.pop(0))
        queue = [root]
        while queue:
            p = queue.pop(0)
            if nodes:
                node = nodes.pop(0)
                if node:
                    queue.append(self.insert_left(p, node))
            if nodes:
                node = nodes.pop(0)
                if node:
                    queue.append(self.insert_right(p, node))

        return root

    def insert_left(self, root, left):
        new = TreeNode(left)
        root.left = new
        return new

    def insert_right(self, root, right):
        new = TreeNode(right)
        root.right = new
        return new

    def


class Solution:
    def __init__(self):
        self.first_node = None
        self.second_node = None
        self.last_node = TreeNode(-2 ** 32)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.find_node(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val

    def find_node(self, root):
        if not root:
            return
        if root.left:
            self.find_node(root.left)

        if not self.first_node and self.last_node.val >= root.val:
            self.first_node = self.last_node
        if self.first_node and self.last_node.val >= root.val:
            self.second_node = root

        self.last_node = root
        if root.right:
            self.find_node(root.right)


if __name__ == '__main__':
    nodes = [1, 3, None, None, 2]
    root = createTree().create(nodes)
    Solution().recoverTree(root)





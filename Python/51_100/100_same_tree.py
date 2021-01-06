# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution1:
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


if __name__ == '__main__':
    p = [1, 2, 3]
    q = [1, 2, 3]
    root_p = createTree().create(p)
    root_q = createTree().create(q)
    print(Solution().isSameTree(root_p, root_q))
    print(Solution1().isSameTree(root_p, root_q))

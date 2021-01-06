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
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        money = root.val
        if root.left:
            money += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money += self.rob(root.right.left) + self.rob(root.right.right)

        return max(money, self.rob(root.left) + self.rob(root.right))


class Solution1:
    def __init__(self):
        self.dic = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root in self.dic:
            return self.dic[root]
        money = root.val
        if root.left:
            money += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money += self.rob(root.right.left) + self.rob(root.right.right)
        res = max(money, self.rob(root.left) + self.rob(root.right))
        self.dic[root] = res

        return res


class Solution2:
    def rob(self, root: TreeNode) -> int:
        res = self.my_rob(root)
        return max(res[0], res[1])

    def my_rob(self, root):
        res = [0, 0]
        if not root:
            return res
        left = self.my_rob(root.left)
        right = self.my_rob(root.right)
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = left[0] + right[0] + root.val

        return res


if __name__ == '__main__':
    nodes = [3, 2, 3, None, 3, None, 1]
    root = createTree().create(nodes)
    print(Solution().rob(root))
    print(Solution1().rob(root))
    print(Solution2().rob(root))

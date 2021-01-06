package leetcode.demo_101_150;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Demo_102_BinaryTreeLevelOrderTraversal {
    public static void main(String[] args) {
        int[] nums = {9, 3, 20, -1, -1, 15, 7};
        TreeNode root = MyTree.create(nums);
        System.out.println(new Solution102().levelOrder(root));
    }
}

class Solution102 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) return new LinkedList<>();

        List<List<Integer>> res = new LinkedList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int count = queue.size();
            List<Integer> temp = new LinkedList<>();
            for (int i = 0; i < count; i++) {
                TreeNode node = queue.poll();
                if (node == null) throw new AssertionError();
                temp.add(node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            res.add(temp);
        }
        return res;
    }
}
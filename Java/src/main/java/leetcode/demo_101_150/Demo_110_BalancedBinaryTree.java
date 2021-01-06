package leetcode.demo_101_150;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

public class Demo_110_BalancedBinaryTree {
    public static void main(String[] args) {
        int[] nums = {1, 2, 2, 3, 3, -1, -1, 4, 4};
        TreeNode root = MyTree.create(nums);
        System.out.println(new Solution110().isBalanced(root));
    }
}

class Solution110 {
    public boolean isBalanced(TreeNode root) {
        return height(root) >= 0;
    }

    private int height(TreeNode root) {
        if (root == null) return 0;
        int left = height(root.left);
        int right = height(root.right);
        if (left >= 0 && right >= 0 && Math.abs(left - right) <= 1) {
            return Math.max(left, right) + 1;
        } else {
            return -1;
        }
    }
}
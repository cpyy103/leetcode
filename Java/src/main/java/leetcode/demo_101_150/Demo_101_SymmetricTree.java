package leetcode.demo_101_150;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

public class Demo_101_SymmetricTree {
    public static void main(String[] args) {
        int[] nums = {1, 2, 2, 3, 4, 4, 3};
        TreeNode root = MyTree.create(nums);
        System.out.println(new Solution101().isSymmetric(root));
    }
}

class Solution101 {
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }

    private boolean isMirror(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        else if (p == null || q == null) return false;

        if (p.val == q.val) return isMirror(p.left, q.right) && isMirror(p.right, q.left);
        else return false;
    }
}

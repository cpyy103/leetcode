package leetcode.demo_51_100;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

public class Demo_100_SameTree {
    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {1, -1, 2};
        TreeNode root1 = MyTree.create(nums1);
        TreeNode root2 = MyTree.create(nums2);
        System.out.println(new Solution100().isSameTree(root1, root2));
    }
}

class Solution100 {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        else if (p == null || q == null) return false;

        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}
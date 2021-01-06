package leetcode.demo_501_550;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

public class Demo_538_ConvertBstToGreaterTree {
    public static void main(String[] args) {
        int[] val = {5,2,13};
        TreeNode root = MyTree.create(val);
        TreeNode root1 = new Solution538().convertBST(root);
        MyTree.levelOrder(root1);
    }
}

class Solution538 {
    public int num = 0;

    public TreeNode convertBST(TreeNode root) {
        preOrder(root);
        return root;
    }

    public void preOrder(TreeNode root) {
        if (root == null) return;
        preOrder(root.right);
        root.val += num;
        num = root.val;
        preOrder(root.left);
    }
}
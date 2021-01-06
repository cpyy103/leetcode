package leetcode.demo_601_650;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

public class Demo_617_MergeTwoBinaryTrees {
    public static void main(String[] args) {
        int[] val1 = {1, 3, 2, 5};
        int[] val2 = {2, 1, 3, -1, 4, -1, 7};
        TreeNode t1 = MyTree.create(val1);
        TreeNode t2 = MyTree.create(val2);
        TreeNode res = new Solution617().mergeTrees(t1, t2);
        MyTree.levelOrder(res);
    }
}

class Solution617 {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 == null) return t2;
        else if (t2 == null) return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
    }
}
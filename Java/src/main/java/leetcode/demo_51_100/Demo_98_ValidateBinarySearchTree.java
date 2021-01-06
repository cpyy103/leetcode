package leetcode.demo_51_100;


import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

public class Demo_98_ValidateBinarySearchTree {
    public static void main(String[] args) {
        int[] nums = {5, 1, 4, -1, -1, 3, 6};
        TreeNode root = MyTree.create(nums);
        System.out.println(new Solution98().isValidBST(root));
    }
}


class Solution98 {
    double last = -Double.MAX_VALUE;

    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        if (isValidBST(root.left)) {
            if (last < root.val) {
                last = root.val;
                return isValidBST(root.right);
            }
        }
        return false;
    }


}
package leetcode.demo_101_150;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

public class Demo_114_FlattenBinaryTreeToLinkedList {
    public static void main(String[] args) {
        int[] val = {1, 2, 5, 3, 4, -1, 6};
        TreeNode root = MyTree.create(val);
        new Solution114().flatten(root);
        MyTree.levelOrder(root);
    }
}

class Solution114 {
    public void flatten(TreeNode root) {
        if (root == null) return;
        flatten(root.left);
        flatten(root.right);

        TreeNode temp = root.right; // 保存右子树
        root.right = root.left; // 将左子树放到右子树上
        root.left = null;   // 将左子树设为空
        while (root.right != null) root = root.right; // 找到现有右子树的最后一个节点
        root.right = temp;  // 将原来的右子树挂在右子树上
    }
}
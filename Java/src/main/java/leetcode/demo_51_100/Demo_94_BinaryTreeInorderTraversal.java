package leetcode.demo_51_100;


import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Demo_94_BinaryTreeInorderTraversal {
    public static void main(String[] args) {
        int[] tree = {1, -1, 2, 3};
        TreeNode root = MyTree.create(tree);
        System.out.println(new Solution94().inorderTraversal(root));
        System.out.println(new Solution94_2().inorderTraversal(root));
    }


}


class Solution94 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        while (!stack.isEmpty() || cur != null) {
            if (cur != null) {
                stack.add(cur);
                cur = cur.left;
            } else {
                cur = stack.pop();
                res.add(cur.val);
                cur = cur.right;
            }
        }
        return res;

    }
}

class Solution94_2 {
    List<Integer> res = new ArrayList<>();

    public List<Integer> inorderTraversal(TreeNode root) {
        inorder(root);
        return res;
    }

    public void inorder(TreeNode root) {
        if (root != null) {
            inorder(root.left);
            res.add(root.val);
            inorder(root.right);
        }
    }
}
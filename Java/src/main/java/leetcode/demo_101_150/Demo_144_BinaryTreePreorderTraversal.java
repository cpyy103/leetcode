package leetcode.demo_101_150;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Demo_144_BinaryTreePreorderTraversal {
    public static void main(String[] args) {
        int[] val = {1, -1, 2, 3};
        TreeNode root = MyTree.create(val);
        System.out.println(new Solution144().preorderTraversal(root));
        System.out.println(new Solution144_2().preorderTraversal(root));
    }
}

class Solution144 {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        while (!stack.isEmpty() || cur != null) {
            if (cur != null) {
                res.add(cur.val);
                stack.push(cur);
                cur = cur.left;
            } else {
                cur = stack.pop();
                cur = cur.right;
            }
        }
        return res;
    }
}

class Solution144_2 {
    List<Integer> res = new ArrayList<>();

    public List<Integer> preorderTraversal(TreeNode root) {
        preorder(root);
        return res;
    }

    public void preorder(TreeNode root) {
        if (root != null) {
            res.add(root.val);
            preorder(root.left);
            preorder(root.right);
        }
    }
}
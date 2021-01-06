package leetcode.demo_101_150;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

public class Demo_145_BinaryTreePostorderTraversal {
    public static void main(String[] args) {
        int[] val = {1, -1, 2, 3};
        TreeNode root = MyTree.create(val);
        System.out.println(new Solution145().postorderTraversal(root));
        System.out.println(new Solution145_2().postorderTraversal(root));
    }
}

class Solution145 {
    public List<Integer> postorderTraversal(TreeNode root) {
        TreeNode cur = root;
        TreeNode pre = null;
        LinkedList<Integer> res = new LinkedList<>();
        Stack<TreeNode> stack = new Stack<>();
        while (!stack.isEmpty() || cur != null) {
            if (cur != null) {
                stack.add(cur);
                cur = cur.left;
            } else {
                cur = stack.peek();
                if (cur.right == null || cur.right == pre) {
                    res.add(cur.val);
                    pre = cur;
                    stack.pop();
                    cur = null;
                } else {
                    cur = cur.right;
                }
            }
        }
        return res;
    }
}

class Solution145_2 {
    List<Integer> res = new ArrayList<>();

    public List<Integer> postorderTraversal(TreeNode root) {
        postorder(root);
        return res;
    }

    public void postorder(TreeNode root) {
        if (root != null) {
            postorder(root.left);
            postorder(root.right);
            res.add(root.val);
        }
    }
}
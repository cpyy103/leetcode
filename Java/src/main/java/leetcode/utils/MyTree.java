package leetcode.utils;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class MyTree {
//    按照层序建树，空节点用-1表示
    public static TreeNode create(int[] val) {
        int count = 0;
        TreeNode root = new TreeNode(val[count++]);
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (count < val.length) {
                int v = val[count++];
                if (v != -1) {
                    TreeNode newNode = new TreeNode(v);
                    queue.add(newNode);
                    node.left = newNode;
                }

                if (count == val.length) break;

                v = val[count++];
                if (v != -1) {
                    TreeNode newNode = new TreeNode(v);
                    queue.add(newNode);
                    node.right = newNode;
                }
            }
        }
        return root;
    }

    public static void levelOrder(TreeNode root) {
        if (root == null) return;
        List<List<Integer>> res = new LinkedList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            int count = queue.size();
            List<Integer> temp = new LinkedList<>();
            for (int i = 0; i < count; i++) {
                TreeNode node = queue.poll();
                if (node == null) throw new AssertionError();
                temp.add(node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            res.add(temp);
        }
        System.out.println(res);
    }
}


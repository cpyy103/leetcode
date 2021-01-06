package leetcode.demo_101_150;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Demo_107_BinaryTreeLevelOrderTraversalII {
    public static void main(String[] args) {
        int[] val = {3, 9, 20, -1, -1, 15, 7};
        TreeNode root = MyTree.create(val);
        System.out.println(new Solution107().levelOrderBottom(root));
    }

}

class Solution107 {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new LinkedList<>();
        if (root == null) {
            return res;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            List<Integer> oneLevel = new ArrayList<>();
            int count = queue.size();
            for (int i = 0; i < count; i++) {
                TreeNode node = queue.poll();
                assert node != null;
                oneLevel.add(node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            res.add(0, oneLevel);
        }
        return res;
    }


}




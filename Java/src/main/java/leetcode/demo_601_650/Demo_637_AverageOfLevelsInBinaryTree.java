package leetcode.demo_601_650;

import leetcode.utils.MyTree;
import leetcode.utils.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Demo_637_AverageOfLevelsInBinaryTree {
    public static void main(String[] args) {
        int[] val = {3, 9, 20, -1, -1, 15, 7};
        TreeNode root = MyTree.create(val);
        System.out.println(new Solution736().averageOfLevels(root));
    }
}

class Solution736 {
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> list = new LinkedList<>();
        list.add(root);
        while (list.size() != 0) {
            int len = list.size();
            double sum = 0;
            for (int i = 0; i < len; i++) {
                TreeNode node = list.poll();
                sum += node.val;
                if (node.left != null) list.add(node.left);
                if (node.right != null) list.add(node.right);

            }
            res.add(sum / len);
        }
        return res;
    }
}
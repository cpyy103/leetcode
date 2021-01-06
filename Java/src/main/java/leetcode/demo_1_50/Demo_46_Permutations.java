package leetcode.demo_1_50;

import java.util.ArrayList;
import java.util.List;

public class Demo_46_Permutations {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        System.out.println(new Solution46().permute(nums));
    }
}


class Solution46 {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int[] visited = new int[nums.length];
        dfs(res, nums, new ArrayList<Integer>(), visited);
        return res;

    }

    private void dfs(List<List<Integer>> res, int[] nums, List<Integer> temp, int[] visited) {
        if (temp.size() == nums.length) {
            res.add(new ArrayList<>(temp));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (visited[i] == 1) continue;
            visited[i] = 1;
            temp.add(nums[i]);
            dfs(res, nums, temp, visited);
            visited[i] = 0;
            temp.remove(temp.size() - 1);
        }
    }
}



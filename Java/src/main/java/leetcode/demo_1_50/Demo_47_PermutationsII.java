package leetcode.demo_1_50;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Demo_47_PermutationsII {
    public static void main(String[] args) {
        int[] nums = {1, 1, 2};
        Arrays.sort(nums);
        System.out.println(new Solution47().permuteUnique(nums));
    }
}

class Solution47 {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int[] visit = new int[nums.length];
        dfs(res, nums, new ArrayList<Integer>(), visit);
        return res;
    }

    private void dfs(List<List<Integer>> res, int[] nums, List<Integer> temp, int[] visited) {
        if (temp.size() == nums.length) {
            res.add(new ArrayList<>(temp));
            return;
        }
        for (int i = 0; i < nums.length; i++) {
            if (visited[i] == 1 || (i > 0 && nums[i] == nums[i - 1] && visited[i - 1] == 0)) continue;
            visited[i] = 1;
            temp.add(nums[i]);
            dfs(res, nums, temp, visited);
            visited[i] = 0;
            temp.remove(temp.size() - 1);
        }
    }
}
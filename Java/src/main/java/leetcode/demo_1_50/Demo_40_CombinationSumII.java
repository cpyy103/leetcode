package leetcode.demo_1_50;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Demo_40_CombinationSumII {
    public static void main(String[] args) {
        int[] candidates = {10, 1, 2, 7, 6, 1, 5};
        int target = 8;
        System.out.println(new Solution40().combinationSum2(candidates, target));
    }
}

class Solution40 {
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        int n = candidates.length;
        dfs(candidates, 0, target, new ArrayList<>());
        return res;

    }

    private void dfs(int[] candidates, int start, int target, List<Integer> temp) {
        if (target < 0) return;
        if (target == 0) {
            res.add(new ArrayList<>(temp));
            return;
        }

        for (int i = start; i < candidates.length; i++) {
            if (i > start && candidates[i] == candidates[i - 1]) continue;
            temp.add(candidates[i]);
            dfs(candidates, i + 1, target - candidates[i], temp);
            temp.remove(temp.size() - 1);
        }
    }
}

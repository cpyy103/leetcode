package leetcode.demo_1_50;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Demo_39_CombinationSum {
    public static void main(String[] args) {
        int[] candidates = {2, 3, 6, 7};
        int target = 7;
        System.out.println(new Solution39().combinationSum(candidates, target));
    }
}

class Solution39 {
    List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        int n = candidates.length;
        dfs(candidates, 0, target, new ArrayList<Integer>());
        return res;
    }

    private void dfs(int[] candidates, int start, int target, List<Integer> temp) {
        if (target < 0) return;
        if (target == 0) {
            res.add(new ArrayList<>(temp));
            return;
        }
        for (int i = start; i < candidates.length; i++) {
            temp.add(candidates[i]);
            // 下一个起点仍然可以为start，实现了重复使用
            dfs(candidates, i, target - candidates[i], temp);
            temp.remove(temp.size() - 1);
        }
    }
}
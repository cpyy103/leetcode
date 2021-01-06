package leetcode.demo_51_100;

import java.util.ArrayList;
import java.util.List;

public class Demo_78_Subsets {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        System.out.println(new Solution78().subsets(nums));
        System.out.println(new Solution78_2().subsets(nums));
    }
}

class Solution78 {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        res.add(new ArrayList<>());

        for (int i = 0; i < nums.length; i++) {
            int size = res.size();
            for (int j = 0; j < size; j++) {
                List<Integer> temp = new ArrayList<>(res.get(j));
                temp.add(nums[i]);
                res.add(temp);
            }
        }
        return res;

    }
}

class Solution78_2 {
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        dfs(nums, new ArrayList<>(), 0);
        res.add(new ArrayList<>());
        return res;

    }

    private void dfs(int[] nums, List<Integer> temp, int x) {
        for (int i = x; i < nums.length; i++) {
            temp.add(nums[i]);
            res.add(new ArrayList<>(temp));
            dfs(nums, temp, i + 1);
            temp.remove(temp.size() - 1);
        }
    }
}
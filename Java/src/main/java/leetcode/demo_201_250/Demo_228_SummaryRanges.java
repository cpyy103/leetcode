package leetcode.demo_201_250;

import java.util.ArrayList;
import java.util.List;

public class Demo_228_SummaryRanges {
    public static void main(String[] args) {
        int[] nums = {0, 1, 2, 4, 5, 7};
        System.out.println(new Solution228().summaryRanges(nums));
    }
}

class Solution228 {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        int i = 0;
        int start = 0;
        int end = 0;
        while (i < nums.length) {
            start = i;
            while (i + 1 < nums.length && nums[i + 1] == nums[i] + 1) i++;
            end = i;
            i++;

            if (start < end) {
                res.add(nums[start] + "->" + nums[end]);
            } else {
                res.add("" + nums[start]);
            }
        }
        return res;
    }
}
package leetcode.demo_51_100;

public class Demo_53_MaximumSubarray {
    public static void main(String[] args) {
        int[] nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        System.out.println(new Solution53().maxSubArray(nums));
    }
}


class Solution53 {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int sum = 0;
        for (int num : nums) {
            if (sum > 0) sum += num;
            else sum = num;

            res = Math.max(res, sum);

        }
        return res;
    }
}
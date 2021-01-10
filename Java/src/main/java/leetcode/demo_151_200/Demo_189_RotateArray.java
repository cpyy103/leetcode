package leetcode.demo_151_200;

import java.util.Arrays;

public class Demo_189_RotateArray {
    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;

        new Solution().rotate(nums, k);
        System.out.println(Arrays.toString(nums));

        nums = new int[]{1, 2, 3, 4, 5, 6, 7};
        new Solution1().rotate(nums, k);
        System.out.println(Arrays.toString(nums));

        nums = new int[]{1, 2, 3, 4, 5, 6, 7};
        new Solution2().rotate(nums, k);
        System.out.println(Arrays.toString(nums));
    }
}

class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        for (int i = 0; i < k; i++) {
            int temp = nums[n - 1];
            System.arraycopy(nums, 0, nums, 1, n - 1);
//            for(int j = nums.length-1;j>0;j--){
//                nums[j] = nums[j-1];
//            }
            nums[0] = temp;
        }
    }
}

class Solution1 {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;

        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[end];
            nums[end--] = nums[start];
            nums[start++] = temp;
        }
    }
}

class Solution2 {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;

        int start = 0;
        while (start < nums.length && k != 0) {
            //当k=0时，说明剩下的数刚好完全正确，不需要交换了
            // 每次从start开始的k个数与最后的k个数进行交换
            for (int i = 0; i < k; i++) {
                swap(nums, start + i, nums.length - k + i);
            }
            start += k; // 每次循环确定k个数，start右移k个位置
            n -= k; // 剩下的未确定的数在减少k个
            k %= n; // n在减小，所以要取余
        }
    }

    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }

}
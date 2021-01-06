package leetcode.demo_1_50;

public class Demo_42_TrappingRainWater {
    public static void main(String[] args) {
        int[] height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
        System.out.println(new Solution42().trap(height));
    }
}

class Solution42 {
    public int trap(int[] height) {
        if (height.length < 2) return 0;
        int left = 0;
        int right = height.length - 1;
        int maxLeft = height[left];
        int maxRight = height[right];

        int res = 0;
        while (left < right) {
            maxLeft = Math.max(maxLeft, height[left]);
            maxRight = Math.max(maxRight, height[right]);
            if (maxLeft < maxRight) {
                res += maxLeft - height[left];
                left++;
            } else {
                res += maxRight - height[right];
                right--;
            }
        }
        return res;
    }
}
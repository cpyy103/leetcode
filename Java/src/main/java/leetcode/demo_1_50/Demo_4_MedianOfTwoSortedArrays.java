package leetcode.demo_1_50;

public class Demo_4_MedianOfTwoSortedArrays {
    public static void main(String[] args) {
        int[] nums1 = {1, 2};
        int[] nums2 = {3, 4};

        System.out.println(new Solution4().findMedianSortedArrays(nums1, nums2));
    }
}


class Solution4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }

        int m = nums1.length;
        int n = nums2.length;

        int size = m + n;
        int cutL = 0;
        int cutR = m;
        int cut1, cut2;

        while (true) {
            cut1 = (cutR - cutL) / 2 + cutL;
            cut2 = size / 2 - cut1;

            int left_1 = cut1 != 0 ? nums1[cut1 - 1] : Integer.MIN_VALUE;
            int left_2 = cut2 != 0 ? nums2[cut2 - 1] : Integer.MIN_VALUE;
            int right_1 = cut1 != m ? nums1[cut1] : Integer.MAX_VALUE;
            int right_2 = cut2 != n ? nums2[cut2] : Integer.MAX_VALUE;

            if (left_1 > right_2) cutR = cut1 - 1;
            else if (left_2 > right_1) cutL = cut1 + 1;
            else {
                if (size % 2 == 0) {
                    int left = Math.max(left_1, left_2);
                    int right = Math.min(right_1, right_2);
                    return ((double) (left + right)) / 2;
                } else {
                    return (double) Math.min(right_1, right_2);
                }
            }

        }

    }
}




package leetcode.demo_301_350;

public class Demo_327_CountOfRangeSum {
    public static void main(String[] args) {
        int[] nums = {2,-1,4,3,-4,2,-1,1};
        int lower = -2;
        int upper = 2;
//        System.out.println(new Solution327().countRangeSum(nums, lower, upper));
        System.out.println(new Solution327_1().countRangeSum(nums, lower, upper));
    }
}

class Solution327 {
    public int countRangeSum(int[] nums, int lower, int upper) {
        int res = 0;
        for (int i = 0; i < nums.length; i++) {
            long sum = 0;
            for (int j = i; j < nums.length; j++) {
                sum += nums[j];
                if (lower <= sum && sum <= upper) res++;
            }
        }
        return res;
    }
}

class Solution327_1 {
    public int countRangeSum(int[] nums, int lower, int upper) {
        long s = 0;
        long[] sum = new long[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            s += nums[i];
            sum[i + 1] = s;
        }
        return countRangeSumRecursive(sum, lower, upper, 0, sum.length-1);
    }

    public int countRangeSumRecursive(long[] sum, int lower, int upper, int left, int right) {
//        System.out.println("left "+left+",right: "+right);
        if (left == right) {
            System.out.println("left "+left+",right: "+right+", return 0");
            return 0;
        } else {
            System.out.println("left "+left+",right: "+right);
            int mid = (left + right) / 2;
            int n1 = countRangeSumRecursive(sum, lower, upper, left, mid);
            System.out.println("n1: "+n1);
            int n2 = countRangeSumRecursive(sum, lower, upper, mid + 1, right);
            System.out.println("n2: "+n2);
            int res = n1 + n2;

            int i = left;
            int l = mid + 1;
            int r = mid + 1;
            System.out.println("left: "+String.valueOf(i));
            while (i <= mid) {
                while (l <= right && sum[l] - sum[i] < lower) l++;
                while (r <= right && sum[r] - sum[i] <= upper) r++;
                System.out.println("l: "+l+", r: "+r+", res_: "+(r-l));
                res += r - l;
                i++;
            }
            System.out.println("res: "+res);
            int[] sorted = new int[right - left + 1];
            int p1 = left;
            int p2 = mid + 1;
            int p = 0;
            while (p1 <= mid || p2 <= right) {
                if (p1 > mid) {
                    sorted[p++] = (int) sum[p2++];
                } else if (p2 > right) {
                    sorted[p++] = (int) sum[p1++];
                } else {
                    if (sum[p1] < sum[p2]) {
                        sorted[p++] = (int) sum[p1++];
                    } else {
                        sorted[p++] = (int) sum[p2++];
                    }
                }
            }
            for (int j = 0; j < sorted.length; j++) {
                sum[left + j] = sorted[j];
            }
            return res;
        }

    }
}
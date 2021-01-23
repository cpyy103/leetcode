package leetcode.demo_951_1000;

import java.util.LinkedList;
import java.util.List;

public class Demo_989_AddToArrayFormOfInteger {
    public static void main(String[] args) {
        int[] A = {1, 2, 0, 0};
        int K = 34;
        System.out.println(new Solution989().addToArrayForm(A, K));
    }
}

class Solution989 {
    public List<Integer> addToArrayForm(int[] A, int K) {
        LinkedList<Integer> res = new LinkedList<>();
        int n = K;
        for (int i = A.length - 1; i >= 0 || n > 0; i--) {
            if (i >= 0) {
                n += A[i];
            }
            res.addFirst(n % 10);
            n /= 10;

        }
        return res;
    }
}
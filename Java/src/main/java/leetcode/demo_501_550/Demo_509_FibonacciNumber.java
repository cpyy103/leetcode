package leetcode.demo_501_550;

public class Demo_509_FibonacciNumber {
    public static void main(String[] args) {
        int n = 10;
        System.out.println(new Solution509().fib(n));
        System.out.println(new Solution509_1().fib(n));
        System.out.println(new Solution509_2().fib(n));
    }
}

class Solution509 {
    public int fib(int n) {
        if (n == 0 || n == 1) return n;
        return fib(n - 1) + fib(n - 2);
    }
}

class Solution509_1 {
    public int fib(int n) {
        if (n == 0 || n == 1) return n;
        int[] arr = new int[n + 1];
        arr[0] = 0;
        arr[1] = 1;
        for (int i = 2; i < n + 1; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
        }
        return arr[n];
    }
}

class Solution509_2 {
    public int fib(int n) {
        if (n == 0 || n == 1) return n;
        int x = 0;
        int y = 1;
        int z = 1;

        for (int i = 0; i < n - 1; i++) {
            z = x + y;
            x = y;
            y = z;
        }
        return z;
    }
}
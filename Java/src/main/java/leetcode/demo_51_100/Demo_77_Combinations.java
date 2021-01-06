package leetcode.demo_51_100;

import java.util.LinkedList;
import java.util.List;

public class Demo_77_Combinations {
    public static void main(String[] args) {
        int n = 4;
        int k = 2;
        System.out.println(new Solution77().combine(n, k));
    }
}

class Solution77 {
    List<List<Integer>> res = new LinkedList<>();
    List<Integer> temp = new LinkedList<>();

    public List<List<Integer>> combine(int n, int k) {
        dfs(n, k, temp, 0);
        return res;

    }

    private void dfs(int n, int k, List<Integer> temp, int x) {
        if (temp.size() == k) {
            res.add(new LinkedList<>(temp));
            return;
        }
        for (int i = x + 1; i <= n; i++) {
            temp.add(i);
            dfs(n, k, temp, i);
            temp.remove(temp.size() - 1);
        }
    }
}
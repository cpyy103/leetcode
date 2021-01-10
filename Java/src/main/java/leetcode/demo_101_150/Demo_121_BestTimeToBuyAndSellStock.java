package leetcode.demo_101_150;

public class Demo_121_BestTimeToBuyAndSellStock {
    public static void main(String[] args) {
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println(new Solution121().maxProfit(prices));
    }
}

class Solution121 {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) return 0;
        int minPrice = prices[0];
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            profit = Math.max(profit, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }

        return profit;
    }
}
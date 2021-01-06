package leetcode.demo_151_200;


public class Demo_174_DungeonGame {
    public static void main(String[] args) {
        int[][] dungeon = {{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}};
        System.out.println(new Solution174().calculateMinimumHP(dungeon));
    }
}

class Solution174 {
    public int calculateMinimumHP(int[][] dungeon) {
        int row = dungeon.length;
        int col = dungeon[0].length;
        // 表示某位置上的最小血量
        int[][] dp = new int[row][col];
        // 终点位置的最少血量，至少为1，如果终点位置是负的，则需要大于该数值的绝对值
        // 如果终点为-5，则到达终点时的血量至少为6
        dp[row - 1][col - 1] = Math.max(1, 1 - dungeon[row - 1][col - 1]);
        // 在最后一列上行走
        for (int i = row - 2; i >= 0; i--) {
            dp[i][col - 1] = Math.max(1, dp[i + 1][col - 1] - dungeon[i][col - 1]);
        }
        // 在最后一行上行走
        for (int i = col - 2; i >= 0; i--) {
            dp[row - 1][i] = Math.max(1, dp[row - 1][i + 1] - dungeon[row - 1][i]);
        }

        for (int i = row - 2; i >= 0; i--) {
            for (int j = col - 2; j >= 0; j--) {
                dp[i][j] = Math.max(1, Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]);
            }
        }

        return dp[0][0];
    }
}
package leetcode.demo_1201_1250;

public class Demo_1232_CheckIfItIsAStraightLine {
    public static void main(String[] args) {
        int[][] coordinates = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}};
        System.out.println(new Solution1232().checkStraightLine(coordinates));

    }
}

class Solution1232 {
    public boolean checkStraightLine(int[][] coordinates) {
        for (int i = 2; i < coordinates.length; i++) {
            if ((coordinates[1][1] - coordinates[0][1]) * (coordinates[i][0] - coordinates[0][0]) != (coordinates[i][1] - coordinates[0][1]) * (coordinates[1][0] - coordinates[0][0]))
                return false;
        }
        return true;
    }
}
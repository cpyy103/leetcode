package leetcode.demo_801_850;

import java.util.ArrayList;
import java.util.List;

public class Demo_830_PositionsOfLargeGroups {
    public static void main(String[] args) {
        String s = "abbxxxxzzy";
        System.out.println(new Solution830().largeGroupPositions(s));
    }
}

class Solution830 {
    public List<List<Integer>> largeGroupPositions(String s) {
        List<List<Integer>> res = new ArrayList<>();
        int start = 0;
        int end = 0;
        while (start < s.length()) {
            end = start + 1;
            while (end < s.length() && s.charAt(start) == s.charAt(end)) {
                end++;
            }
            if (end - start >= 3) {
                List<Integer> temp = new ArrayList<>();
                temp.add(start);
                temp.add(end - 1);
                res.add(temp);
            }
            start = end;
        }
        return res;
    }
}
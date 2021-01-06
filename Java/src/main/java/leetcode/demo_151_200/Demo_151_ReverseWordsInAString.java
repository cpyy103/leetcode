package leetcode.demo_151_200;

public class Demo_151_ReverseWordsInAString {
    public static void main(String[] args) {
        String s = "Hello World! ";
        System.out.println(s.substring(1, 3));
        System.out.println(new Solution151().reverseWords(s));
    }
}

class Solution151 {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        int right = s.length() - 1;
        int left = right;
        while (left >= 0) {
            while (left >= 0 && s.charAt(left) == ' ') right = --left;
            while (left >= 0 && s.charAt(left) != ' ') left--;
            if (left != right) res.append(s, left + 1, right + 1).append(" ");
        }

        if (res.length() != 0) res.deleteCharAt(res.length() - 1);
        return res.toString();
    }
}
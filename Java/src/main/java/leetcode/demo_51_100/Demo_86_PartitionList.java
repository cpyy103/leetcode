package leetcode.demo_51_100;

public class Demo_86_PartitionList {
    public static void main(String[] args) {
        int[] list = {1, 4, 4, 3, 5, 2};
        int x = 3;
        ListNode dummy = new ListNode();
        ListNode p = dummy;
        for (int i : list) {
            p.next = new ListNode(i);
            p = p.next;
        }

        ListNode res = new Solution86().partition(dummy.next, x);
        while (res != null) {
            System.out.println(res.val);
            res = res.next;
        }

    }
}

class Solution86 {
    public ListNode partition(ListNode head, int x) {
        ListNode head_big = new ListNode();
        ListNode head_small = new ListNode();

        ListNode p_big = head_big;
        ListNode p_small = head_small;

        while (head != null) {
            if (head.val >= x) {
                p_big.next = head;
                p_big = p_big.next;
            } else {
                p_small.next = head;
                p_small = p_small.next;
            }
            head = head.next;
        }

        p_small.next = head_big.next;
        p_big.next = null;

        return head_small.next;
    }
}


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
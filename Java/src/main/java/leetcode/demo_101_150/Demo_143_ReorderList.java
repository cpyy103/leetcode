package leetcode.demo_101_150;

import leetcode.utils.ListNode;

import java.util.LinkedList;

public class Demo_143_ReorderList {
    public static void main(String[] args) {
        int[] val = {1, 2, 3, 4, 5};
        ListNode head = new ListNode(-1);
        ListNode p = head;
        for (int i : val) {
            p.next = new ListNode(i);
            p = p.next;
        }

        new Solution143().reorderList(head.next);

        p = head.next;
        while (p != null) {
            System.out.println(p.val);
            p = p.next;
        }
    }
}

class Solution143 {
    public void reorderList(ListNode head) {
        LinkedList<ListNode> queue = new LinkedList<>();
        ListNode cur = head;
        while (cur != null) {
            queue.addLast(cur);
            cur = cur.next;
        }
        while (!queue.isEmpty()) {
            if (cur == null) {
                cur = queue.pollFirst();
            } else {
                cur.next = queue.pollFirst();
                cur = cur.next;
            }
            cur.next = queue.pollLast();
            cur = cur.next;
        }
        if (cur != null) {
            cur.next = null;
        }

    }
}
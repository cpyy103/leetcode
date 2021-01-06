package leetcode.demo_101_150;

import java.util.Map;

public class Demo_146_LruCache {
    public static void main(String[] args) {

    }
}

class LRUCache {
    static class Node{
        int key;
        int value;
        Node pre = null;
        Node next = null;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    Map<Integer, Node> map;
    Node head;
    Node tail;
    int capacity;

    public LRUCache(int capacity) {
        capacity = capacity;
        head.next = tail;
        tail.pre = head;

    }

    public int get(int key) {
        if (!map.containsKey(key)) return -1;
        Node node = map.get(key);
        moveToHead(node);
        return node.value;

    }

    public void put(int key, int value) {
        if(map.containsKey(key)){
            Node node = map.get(key);
            node.value = value;
            moveToHead(node);
        }else{
            Node node = new Node(key, value);
            addToHead(node);
            map.put(key, node);
            capacity--;
            if (capacity==0){
                Node removed = remove_tail();
                map.remove(removed.key);
                capacity++;
            }
        }

    }
    private void moveToHead(Node node){
        remove(node);
        addToHead(node);
    }
    private void remove(Node node){
        node.pre.next = node.next;
        node.next.pre = node.pre;
    }
    private void addToHead(Node node){
        head.next.pre = node;
        node.next = head.next;
        node.pre = head;
        head.next = node;
    }

    private Node remove_tail(){
        Node node = tail.pre;
        remove(node);
        return node;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
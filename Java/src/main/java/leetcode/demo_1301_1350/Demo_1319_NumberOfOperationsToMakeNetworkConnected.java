package leetcode.demo_1301_1350;

public class Demo_1319_NumberOfOperationsToMakeNetworkConnected {
    public static void main(String[] args) {
        int n = 4;
        int[][] connections = {{0, 1}, {0, 2}, {1, 2}};
        System.out.println(new Solution1319().makeConnected(n, connections));
    }
}

class Solution1319 {
    private int[] parent;

    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) return -1;
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int[] connection : connections) {
            union(connection[0], connection[1]);
        }
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (parent[i] == i) {
                count++;
            }
        }

        return count - 1;
    }

    private int find(int node) {
        if (parent[node] == node) return node;
        else return parent[node] = find(parent[node]);
    }

    private void union(int node1, int node2) {
        int root1 = find(node1);
        int root2 = find(node2);
        if (root1 == root2) return;
        parent[root1] = root2;
    }
}
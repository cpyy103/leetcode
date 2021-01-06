package leetcode.demo_301_350;


import java.util.*;

public class Demo_347_TopKFrequentElements {
    public static void main(String[] args) {
        int[] nums = {1, 1, 1, 2, 2, 3};
        int k = 2;
        System.out.println(Arrays.toString(new Solution347().topKFrequent(nums, k)));
        System.out.println(Arrays.toString(new Solution347().topKFrequent_2(nums, k)));


        String a = "123";
        String b = "122";
        System.out.println(a.compareTo(b));
    }
}


class Solution347 {
    // 正常排序
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort((o1, o2) -> o2.getValue() - o1.getValue());

        int[] res = new int[k];
        for (int i = 0; i < k; i++) {
            res[i] = list.get(i).getKey();
        }

        return res;
    }

    // 使用最小堆
    public int[] topKFrequent_2(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        // 最小堆
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> map.get(o1) - map.get(o2));

        for (Integer key : map.keySet()) {
            if (pq.size() < k) {
                pq.add(key);
            } else if (map.get(key) > map.get(pq.peek())) {
                pq.remove();
                pq.add(key);
            }
        }

        int[] res = new int[k];
        int index = k - 1;
        while (!pq.isEmpty()) {
            res[index--] = pq.remove();

        }
        return res;
    }


}


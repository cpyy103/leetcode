from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x - y)

        return -heap[0] if len(heap) == 1 else 0


class Solution1:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = MyHeap(desc=True)
        for stone in stones:
            heap.push(stone)
        print(heap.heap)
        while heap.size > 1:
            x = heap.pop()
            y = heap.pop()
            if x != y:
                heap.push(x - y)

        return heap.top() if heap.size == 1 else 0


class MyHeap:
    def __init__(self, desc=False):
        '''
        初始化
        :param desc: 默认小顶堆
        '''
        self.heap = []
        self.desc = desc

    @property
    def size(self):
        return len(self.heap)

    def top(self):
        if len(self.heap) > 0:
            return self.heap[0]
        return None

    def push(self, element):
        self.heap.append(element)
        self._sift_up(self.size - 1)

    def pop(self):
        self._swap(0, self.size - 1)
        element = self.heap.pop()
        self._sift_down(0)
        return element

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _cmp(self, a, b):
        '''
        当desc为False，表示小顶堆，返回 a < b表示需要进行交换
        当desc为True，表示大顶堆，返回 a > b表示需要进行交换
        :param a:
        :param b:
        :return:
        '''
        return a < b if self.desc else a > b

    def _sift_up(self, index):
        '''
        自下向上调整
        当当前节点和父节点需要调整时，进行调整
        :param index: 当前节点的下标
        :return:
        '''
        while index:
            parent = (index - 1) // 2
            if self._cmp(self.heap[index], self.heap[parent]):
                break

            self._swap(index, parent)
            index = parent

    def _sift_down(self, index):
        '''
        自上向下调整
        当当前节点和左右子节点需要调整时，进行调整
        :param index: 当前节点的下标
        :return:
        '''
        while 2 * index + 1 < self.size:
            cur = index
            left = 2 * index + 1
            right = 2 * index + 2

            if self._cmp(self.heap[cur], self.heap[left]):
                cur = left

            if right < self.size and self._cmp(self.heap[cur], self.heap[right]):
                cur = right

            if cur == index:
                break
            self._swap(cur, index)
            index = cur


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones))
    print(Solution1().lastStoneWeight(stones))




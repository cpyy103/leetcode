class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0  # 现有数据数
        self.cache = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move2head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move2head(node)
        else:
            node = DLinkedNode(key, value)
            self.add2head(node)
            self.cache[key] = node
            self.size += 1
            # 如果大于最大容量，删除最旧数据
            if self.size > self.capacity:
                removed_node = self.remove_tail()
                self.cache.pop(removed_node.key)
                self.size -= 1

    # 将节点移动至头节点后一位位置，表示为最新操作数据
    def move2head(self, node):
        self.remove(node)
        self.add2head(node)

    # 删除节点
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    # 头节点后添加节点
    def add2head(self, node):
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node

    # 删除尾部的前一个节点，表示为删除最旧操作数据
    def remove_tail(self):
        node = self.tail.pre
        self.remove(node)
        return node


if __name__ == '__main__':
    cache = LRUCache(2)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))
    print(cache.put(3, 3))
    print(cache.get(2))
    print(cache.put(4, 4))
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

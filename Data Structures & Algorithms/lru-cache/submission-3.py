class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def remove (self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
        else:
            self.cache[key] = Node(key, value)
            node = self.cache[key]
            if len(self.cache) > self.capacity:
                del self.cache[self.left.next.key]
                self.remove(self.left.next)
        self.insert(node)













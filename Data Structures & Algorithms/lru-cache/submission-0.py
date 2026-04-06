class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(0, 0), Node(0,0)
        self.cap = capacity
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        last = self.right.prev
        self.right.prev = node
        last.next = node
        node.prev = last
        node.next = self.right
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            key = self.left.next.key
            self.remove(self.left.next)
            del self.cache[key]

            

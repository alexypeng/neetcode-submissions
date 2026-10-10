from dataclasses import dataclass

@dataclass
class Node:
    key: int
    val: int
    prev: Optional[Node] = None
    next: Optional[Node] = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node

    def remove(self, node):
        prev, nxt = node.prev, node.next
        node.prev.next, node.next.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        

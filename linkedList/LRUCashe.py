#get : get value of head of list, move head pointer to next and move the original head node to end of list (Most recently used at end)
#put : if too many, remove head  
class Node(object):
    def __init__(self, key, x):
        self.key = key
        self.val = x
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.sentHead = Node(0, 0)
        self.sentTail = Node(0, 0)

        self.sentHead.next = self.sentTail
        self.sentTail.prev = self.sentHead

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insertEnd(self, node):
        prev, next = self.sentTail.prev, self.sentTail
        prev.next, next.prev = next, prev
        node.next, node.prev = next, prev
        

    def get(self, key):
        if key in self.cache:
            n = self.cache[key]
            self._remove(n)
            self._insertEnd(n)
            return n.val
        return -1
    



    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node

        self._insertEnd(node)

        if len(self.cache) > self.cap:
            temp = self.sentHead.next
            self._remove(temp)
            del self.cache[temp.key]


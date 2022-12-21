#User function Template for python3

# design the class in the most optimal way
from collections import deque
import heapq
class CacheEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = CacheEntry(0, 0)  # sentinel node
        self.tail = CacheEntry(0, 0)  # sentinel node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.cache:
            return -1
        entry = self.cache[key]
        self._remove(entry)
        self._add(entry)
        return entry.value

    def set(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        entry = CacheEntry(key, value)
        self._add(entry)
        self.cache[key] = entry
        if len(self.cache) > self.capacity:
            self._evict()

    def _remove(self, entry):
        prev_node = entry.prev
        next_node = entry.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, entry):
        prev_node = self.head
        next_node = self.head.next
        prev_node.next = entry
        next_node.prev = entry
        entry.prev = prev_node
        entry.next = next_node

    def _evict(self):
        last_entry = self.tail.prev
        self._remove(last_entry)
        del self.cache[last_entry.key]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        cap = int(input())  # capacity of the cache
        qry=int(input())  #number of queries
        a = list(map(str, input().strip().split()))  # parent child info in list
        
        lru=LRUCache(cap)
        
       
        i=0
        q=1
        while q<=qry:
            qtyp=a[i]
            
            if qtyp=='SET':
                lru.set(int(a[i+1]),int(a[i+2]))
                i+=3
            elif qtyp=='GET':
                print(lru.get(int(a[i+1])),end=' ')
                i+=2
            q+=1
        print()
# } Driver Code Ends
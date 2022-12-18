#User function Template for python3
from collections import defaultdict
import heapq
from typing import List
class Solution:
    def minimumCost(self, flights: List[List[int]], n : int, k : int) -> int:
        # code here
        adj = defaultdict(list)
        for s, d, w in flights:
            adj[s].append((d,w))
        
        visited = set()
        minheap = [(0,k)]
        
        ans = 0
        
        while minheap:
            wnode,vnode = heapq.heappop(minheap)
            
            if vnode in visited:
                continue
            
            ans = max(ans, wnode)
            visited.add(vnode)
            
            for v, w in adj[vnode]:
                heapq.heappush(minheap, (wnode+w, v))
        return ans if len(visited) == n else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        k = int(input())
        m = int(input())
        flights = []
        for i in range(m):
            u, v, wt = map(int, input().strip().split())
            flights.append([u, v, wt])
        obj = Solution()
        ans = obj.minimumCost(flights, n, k)
        print(ans)
            

# } Driver Code Ends
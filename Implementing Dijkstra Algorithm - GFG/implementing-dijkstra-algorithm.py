import heapq
from collections import defaultdict
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        visited = dict()
        heap = [(0,S)]
        
        while heap:
            w,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited[node] = w
            for j,wj in adj[node]:
                if j not in visited:
                    heapq.heappush(heap, (w+wj, j))
        ans = []
        for i in range(len(adj)):
            ans.append(visited[i])
        return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
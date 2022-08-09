from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        visited = [False] * n
        q = deque()
        q.append(source)
        visited[source] = True
        
        while len(q):
            node = q.popleft()
            if node == destination:
                return True
            for adj in graph[node]:
                if not visited[adj]:
                    q.append(adj)
                    visited[adj] = True
            
        
        return False
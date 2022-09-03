from collections import defaultdict, deque
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        rest = set(restricted)
        
        edge = defaultdict(list)
        for e in edges:
            edge[e[0]].append(e[1])
            edge[e[1]].append(e[0])
        
        q = deque()
        visited = set()
        cnt = 1
        q.append(0)
        visited.add(0)
        
        while q:
            node = q.popleft()
            for neigh in edge[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    if neigh not in rest:
                        cnt += 1
                        q.append(neigh)
        return cnt
        
            
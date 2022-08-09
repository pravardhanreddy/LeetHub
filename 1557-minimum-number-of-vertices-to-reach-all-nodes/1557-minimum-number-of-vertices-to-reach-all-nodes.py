class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = [False] * n
        for e in edges:
            reachable[e[1]] = True
        
        return [i for i in range(n) if not reachable[i]]
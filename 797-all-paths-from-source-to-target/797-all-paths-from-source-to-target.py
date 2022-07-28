class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def travel(graph, i, n, ans, path , visited):
            path.append(i)
            if i == n-1:
                ans.append(path[:])
            else:
                for j in graph[i]:
                    if not visited[j]:
                        visited[j] = True
                        travel(graph, j, n, ans, path, visited)
                        visited[j] = False
            path.pop()
            
            
            
        n = len(graph)
        visited = [False]*n
        ans = []
        path = []
        visited[0] = True
        travel(graph, 0, n, ans, path, visited)
        return ans
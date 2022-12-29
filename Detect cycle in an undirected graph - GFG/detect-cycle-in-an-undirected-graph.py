from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = set()
		def dfs(root, parent, s, visited):
		    if root in visited:
		        return False
            if root in s:
                return True
            s.add(root)
            for i in adj[root]:
                if i != parent and dfs(i, root, s, visited):
                    return True
            visited.add(root)
            return False
            
            
		for v in range(V):
		    s = set()
		    if v not in visited and dfs(v,None, s, visited):
		        return True
        return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
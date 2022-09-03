from collections import defaultdict
class Solution:
    def possibleBipartition(self, n, dislikes):
        g1 = set()
        g2 = set()
        dis = defaultdict(list)
        
        for a,b in dislikes:
            dis[a].append(b)
            dis[b].append(a)
            
        visited = [False for _ in range(n+1)]
        
        stack = [i for i in range(1, n+1)]
        
        while stack:
            i = stack.pop()
            if visited[i]:
                continue
            visited[i] = True
            
            # case 1
            if i in g1:
                for j in dis[i]:
                    if j in g1:
                        return False
                    else:
                        g2.add(j)
                        stack.append(j)
            # case 2
            else:
                if i not in g2:
                    g2.add(i)
                for j in dis[i]:
                    if j in g2:
                        return False
                    else:
                        g1.add(j)
                        stack.append(j)

                
        return True
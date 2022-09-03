from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def search(a,b,d,v, visited, val):
            visited.add(a)
            if (a,b) in v:
                return val*v[(a,b)]
            for newa in d[a]:
                if newa not in visited:
                    res = search(newa, b, d, v, visited, val*v[(a,newa)])
                    if res != -1.0:
                        return res
            return -1.0
        
        d = defaultdict(list)
        v = dict()
        for i in range(len(values)):
            d[equations[i][0]].append(equations[i][1])
            d[equations[i][1]].append(equations[i][0])
            
            v[(equations[i][0], equations[i][1])] = values[i]
            v[(equations[i][1], equations[i][0])] = 1/values[i]
        
        ans = []
        for a, b in queries:
            if a not in d or b not in d:
                ans.append(-1.0)
            
            elif a == b:
                ans.append(1.0)
            
            elif (a,b) in v:
                ans.append(v[(a,b)])
            elif (b,a) in v:
                ans.append(v[(b,a)])
                
            else:
                visited = set()
                ans.append(search(a,b,d,v, visited, 1.0))
        return ans
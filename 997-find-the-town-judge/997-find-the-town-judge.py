from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust)==0:
            return 1
        
        s = set([i for i in range(1, n+1)])
        d = defaultdict(int)
        
        for t in trust:
            s.discard(t[0])
            d[t[1]]+=1
        for ele in d:
            if d[ele] == n-1 and ele in s:
                return ele
        return -1
        
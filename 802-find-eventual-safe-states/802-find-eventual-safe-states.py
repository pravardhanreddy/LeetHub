from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def adjust(i, d, dc, s):
            if i in d:
                for node in d[i]:
                    dc[node] -= 1
                    if dc[node] == 0:
                        s.add(node)
                        adjust(node, d, dc, s)
                d.pop(i)
                        
        
        d = defaultdict(list)
        dc = defaultdict(int)
        s = set()
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                s.add(i)
                adjust(i, d, dc, s)
            else:
                flag = True
                for node in graph[i]:
                    if node not in s:
                        flag = False
                        d[node].append(i)
                        dc[i] += 1
                if flag:
                    s.add(i)
                    adjust(i, d, dc, s)
        
        return sorted(s)
            
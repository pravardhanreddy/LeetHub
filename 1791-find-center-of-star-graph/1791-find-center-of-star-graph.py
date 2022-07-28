class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s = set(edges[0])
        if edges[1][0] in s:
            return edges[1][0]
        else:
            return edges[1][1]
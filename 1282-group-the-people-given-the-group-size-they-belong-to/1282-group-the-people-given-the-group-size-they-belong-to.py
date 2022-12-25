from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        
        ans = []
        
        for g in d:
            if len(d[g]) == g:
                ans.append(d[g])
            else:
                for k in range(0,len(d[g]), g):
                    ans.append(d[g][k:k+g])
        return ans
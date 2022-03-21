class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        d = {}
        
        for i in range(len(s)):
            d[s[i]] = i
        
        m = -1
        l = []
        prev = -1
        
        for i in range(len(s)):
            m = max(m,d[s[i]])
            if i == m:
                l.append(i-prev)
                prev = i
                m = -1            
        rem = len(s) - sum(l)
        if rem > 0:
            l.append(rem)
        return l
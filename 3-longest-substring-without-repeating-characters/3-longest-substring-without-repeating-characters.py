class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sub  = set()
        ending = []
        
        for i,n in enumerate(s):
            if n in sub:
                ending.append(i-l)
                while(s[l] != n):
                    sub.discard(s[l])
                    l += 1
                sub.discard(s[l])
                l += 1
            sub.add(n)
        ending.append(len(sub))
        return max(ending)
        
                
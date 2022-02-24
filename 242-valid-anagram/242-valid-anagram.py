class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        
        for a in s:
            try:
                first[a] += 1
            except:
                first[a] = 1
        for a in t:
            try:
                second[a] += 1
            except:
                second[a] = 1
        sel = first if len(first) > len(second) else second
        
        for a in sel:
            try:
                if first[a] != second[a]:
                    return False
            except:
                return False
        
        return True
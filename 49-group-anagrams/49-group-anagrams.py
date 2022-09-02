class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = dict()
        for s in strs:
            srtd = str(sorted(s))
            if srtd in d:
                d[srtd].append(s)
            else:
                d[srtd] = [s]
        
        return [d[k] for k in d]
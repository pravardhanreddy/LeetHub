class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = {}
        s2 = {}
        
        res = set()
        
        for a in nums1:
            s1[a] = 1
        
        for a in nums2:
            try:
                if s1[a] == 1:
                    res.add(a)
            except:
                s2[a] = 1
        
        for a in nums3:
            try:
                if s1[a] == 1:
                    res.add(a)
            except:
                try:
                    if s2[a] == 1:
                        res.add(a)
                except:
                    pass
        return list(res)
        
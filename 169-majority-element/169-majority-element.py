class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        
        for i in nums:
            try:
                d[i] += 1
            except:
                d[i] = 1
        
        h = 0
        m = 0
        
        for i in d:
            if d[i] > m:
                m = d[i]
                h = i
        
        return h
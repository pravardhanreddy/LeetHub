class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        l = [[] for i in range(len(nums)+1)]
        ans = []
        
        for n in nums:
            d[n] += 1
        
        for n in d:
            l[d[n]].append(n)
        
        for i in range(len(nums), 0, -1):
            ans.extend(l[i])
            if len(ans) == k:
                return ans
        
            
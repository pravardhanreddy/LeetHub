class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            s = set()
            ans = set()
            for i in nums:
                if i in s:
                    ans.add(i)
                else:
                    s.add(i)
            return len(ans)
        else:
            ans = set()
            s = set(nums)
            for i in nums:
                if i+k in s:
                    ans.add(i)
            return len(ans)
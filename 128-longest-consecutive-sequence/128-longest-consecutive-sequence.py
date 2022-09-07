class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans,curr = 1,1
        s = set(nums)
        start = end = s.pop()
        while s:
            if start-1 not in s and end+1 not in s:
                curr = 1
                start = end = s.pop()
            else:
                if start-1 in s:
                    curr += 1
                    s.discard(start-1)
                    start -= 1
                if end+1 in s:
                    curr += 1
                    s.discard(end+1)
                    end += 1
                ans = max(ans, curr)
        return ans
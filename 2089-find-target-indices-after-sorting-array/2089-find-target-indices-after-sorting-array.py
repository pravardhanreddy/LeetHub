class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        others = 0
        count = 0
        ans = []
        for n in nums:
            if n == target:
                count += 1
            elif n < target:
                others += 1
        for i in range(count):
            ans.append(i + others)
        return ans
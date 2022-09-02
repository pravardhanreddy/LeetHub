from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front = [1]
        back = deque()
        back.append(1)
        n = len(nums)
        for i in range(len(nums) - 1):
            front.append(front[i] * nums[i])
            back.appendleft(back[0] * nums[n - i - 1])
        
        return [front[i] * back[i] for i in range(n)]
        
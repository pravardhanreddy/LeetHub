#User function Template for python3
from collections import deque
class Perm:
    def permute(self, nums):
        result = []
        nums = deque(nums)
        if len(nums) == 1:
            return [nums.copy()]
        
        for _ in range(len(nums)):
            n = nums.popleft()
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)
        
        return result
class Solution:
    def find_permutation(self, S):
        # Code here
        obj = Perm()
        inp = []
        for s in S:
            inp.append(s)
        ans = obj.permute(inp)
        
        res = set()
        for a in ans:
            res.add(''.join(a))
        return sorted(list(res))



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends
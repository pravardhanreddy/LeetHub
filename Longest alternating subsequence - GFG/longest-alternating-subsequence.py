#User function Template for python3

class Solution:
	def AlternatingaMaxLength(self, nums):
		# Code here
		if len(nums) == 1:
            return 1
        s = 1 if nums[0] == nums[1] else 2
        prev = nums[1]
        cond = nums[1] > nums[0]
        
        for i in range(2,len(nums)):
            if cond:
                if nums[i] < nums[i-1]:
                    s += 1
                    cond = False
            else:
                if nums[i] > nums[i-1]:
                    s+=1
                    cond = True
        return s
		
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.AlternatingaMaxLength(nums)
		print(ans)

# } Driver Code Ends
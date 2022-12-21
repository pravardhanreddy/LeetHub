

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, arr):
		#Code here
        sarr = sorted(arr)
        d = dict()
        cnt = 0
        for i in range(n):
            if sarr[i] != arr[i]:
                d[sarr[i]] = arr[i]
        
        # remove cycles
        while d:
            s = set()
            node, val  = d.popitem()
            while d and val not in s and val in d:
                cnt += 1
                s.add(val)
                val = d.pop(val)
        
        return cnt


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends
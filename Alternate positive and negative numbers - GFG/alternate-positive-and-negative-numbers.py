#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        # code here
        narr = []
        parr = []
        for i in range(n):
            if arr[i] < 0:
                narr.append(arr[i])
            else:
                parr.append(arr[i])
        p,k = 0,0
        cn = len(narr)
        cp = len(parr)
        i = 0
        while(i<n):
            if(p < cp):
                arr[i] = parr[p]
                i += 1
                p += 1
            if(k < cn ):
                arr[i] = narr[k]
                i += 1
                k += 1
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends
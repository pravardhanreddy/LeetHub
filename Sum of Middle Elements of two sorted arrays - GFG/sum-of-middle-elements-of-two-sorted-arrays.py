#User function Template for python3

class Solution:
	def findMidSum(self, ar1, ar2, n): 
		# code here 
		ans1 = find(ar1, n, ar2, n, n)
		ans2 = find(ar1, n, ar2, n, n + 1)
# 		print(ans1, ans2)
		return  ans1 + ans2 

def find(ar1, a1, ar2, a2, k):
    if a1 <= 0:
        return ar2[k-1]
    if a2 <= 0:
        return ar1[k-1]
        
    if k == 1:
        return min(ar1[0], ar2[0])
    
    i = min(a1, k//2)
    j = min(a2, k//2)
    
    if ar1[i-1] < ar2[j-1]:
        return find(ar1[i:], a1-i, ar2, a2, k-i)
    else:
        return find(ar1, a1, ar2[j:], a2-j, k-j)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ar1=list(map(int, input().strip().split()))
        ar2=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMidSum(ar1, ar2, n)
        print(ans)
        tc=tc-1

# } Driver Code Ends
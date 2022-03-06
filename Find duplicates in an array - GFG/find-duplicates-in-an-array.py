class Solution:
    def duplicates(self, arr, n): 
    	# code here
        s1 = set()
        s2 = set()
        for a in arr:
            if a in s1:
                s2.add(a)
            else:
                s1.add(a)
        return sorted(list(s2)) if len(s2) else [-1]

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends
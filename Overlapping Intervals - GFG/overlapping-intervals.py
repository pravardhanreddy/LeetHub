class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		mylist = []
		for a,b in Intervals:
		    mylist.append((a,0))
		    mylist.append((b,1))
		
		mylist.sort()
# 		print(mylist)
		cnt = 0
		
		start = None
		
		ans = []
		
		for a, b in mylist:
		    if cnt == 0:
	            start = a
	            cnt += 1
	        else:
		        if b == 0:
		            cnt += 1
                else:
                    if cnt == 1:
                        ans.append([start, a])
                    cnt -= 1
        return ans


#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends
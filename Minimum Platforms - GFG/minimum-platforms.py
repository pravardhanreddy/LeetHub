#User function Template for python3
from collections import Counter

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        time = sorted(set(arr+dep))
        a = Counter(arr)
        d = Counter(dep)
        cnt, m = 0,0
        for t in time:
            if t in a:
                cnt += a.pop(t)
                m = max(m,cnt)
            if t in d:
                cnt-=d.pop(t)
        return m

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends
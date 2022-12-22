#User function Template for python3

import collections
class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        ans = []
        d = collections.defaultdict(list)
        for i in range(n-1):
            if arr[i] < arr[i+1]:
                ans.append(arr[i+1])
                s = set()
                for num in d:
                    # print(num, d[num])
                    if num < arr[i+1]:
                        for ind in d[num]:
                            ans[ind] = arr[i+1]
                        s.add(num)
                for num in s:
                    d.pop(num)
            else:
                ans.append(-1)
                d[arr[i]].append(i)
                # print(d)
        ans.append(-1)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends
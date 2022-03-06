#User function Template for python3

def max_sum(a,n):
    #code here
    s=sum(a)
    
    isum = 0
    for i in range(n):
        isum += i*a[i]
    m = 0
    for i in range(n):
        isum = isum - s + ((n)*a[i]) 
        m = max(m,isum)
    return m

#{ 
#  Driver Code Starts
#Initial Template for Python 3


    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr,n))
# } Driver Code Ends
#User function Template for python3
def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    # for p in range(2, n+1):
    #     if prime[p]:
    #         print(p)
    # Add all primes to a set
    s = set()
    for p in range(2, n+1):
        if prime[p]:
            s.add(p)
    return s
    
class Solution:
    def primeDivision(self, N):
        # code here
        s = SieveOfEratosthenes(N)
        l = sorted(list(s))
        for a in l:
            if N-a in s:
                return [a,N-a]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends
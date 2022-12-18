#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        
        if n <= 0:
            return arr2[k-1]
        if m <= 0:
            return arr1[k-1]
        
        if k == 1:
            return min(arr1[0], arr2[0])
        
        
        i = min(n, k//2)
        j = min(m, k//2)
        
        if arr1[i-1] < arr2[j-1]:
            return self.kthElement(arr1[i:], arr2, n-i, m, k-i)
        else:
            return self.kthElement(arr1, arr2[j:], n, m-j, k-j)
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
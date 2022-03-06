#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        p = []
        n = []
        for a in arr:
            if a < 0:
                n.append(a)
            else:
                p.append(a)
        arr[:len(p)] = p
        arr[len(p):] = n

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
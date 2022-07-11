#User function Template for python3


'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    #Function to construct binary tree from parent array.
    def createTree(self,parent,N):
        # your code here
        d = {}# key = value in parent : val = index
        for i in range(-1,N):
            d[i] = []
        for i in range(N):
            d[parent[i]].append(i)
        
        nodes = [Node(i) for i in range(N)]
        
        q = deque()
        q.append(d[-1][0])
        while len(q):
            ind = q.popleft()
            l = d[ind]
            if len(l) == 2:
                nodes[ind].left = nodes[l[0]]
                nodes[ind].right = nodes[l[1]]
                q.append(l[0])
                q.append(l[1])
            elif len(l) == 1:
                nodes[ind].left = nodes[l[0]]
                q.append(l[0])
                
        return nodes[d[-1][0]]
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import  defaultdict

#Contributed by : Nikhil Kumar Singh

'''
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
'''


# Python implementation to construct a Binary Tree from
# parent array

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Function should print the level order of the tree in sorted format
def traverse_level_order(root):
    # Code here
    if root is None:
        return
    que = []
    que.append(root)
    while 1:
        n = len(que)
        if n==0:
            break
        sorted_nodes = [node.key for node in que]
        sorted_nodes.sort()
        print(*sorted_nodes,end=" ")
        while(n>0):
            node = que.pop(0)
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
            n-=1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        a = list(map(int, input().strip().split()))  # parent child info in list
        ob = Solution()
        traverse_level_order(ob.createTree(a,n))
        print()
# } Driver Code Ends
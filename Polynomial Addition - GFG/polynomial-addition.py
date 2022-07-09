#{ 
#Driver Code Starts
# Node Class    
class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, coeff, pwr):
        if self.head == None:
            self.head = node(coeff, pwr)
        else:
            new_node = node(coeff, pwr)
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

def createList(arr, n):
    lis = Linked_List()
    k=0
    for i in range(n):
        lis.insert(arr[k], arr[k+1])
        k+=2
    return lis.head


 # } Driver Code Ends
# your task is to complete this function
'''
 class node:
    def __init__(self, coeff, pwr):
        self.coef = coeff
        self.next = None
        self.power = pwr
'''

class Solution:
    # return a linked list denoting the sum with decreasing value of power
    def addPolynomial(self, poly1, poly2):
        # Code here
        if not poly1:
            return poly2
        if not poly2:
            return poly1
        
        m = max(poly1.power, poly2.power)
        l = [0] * (m+1)
        
        while poly1:
            l[poly1.power] = poly1.coef
            poly1 = poly1.next
        while poly2:
            l[poly2.power] += poly2.coef
            poly2 = poly2.next
        
        n = node(None, None)
        head = n
        
        while len(l):
            coef = l.pop()
            if coef:
                n.next = node(coef, len(l))
                n = n.next
        return head.next

#{ 
#Driver Code Starts.
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly1 = createList(arr, n)
        n = int(input())
        arr = list(map(int, input().strip().split()))
        poly2 = createList(arr, n)
        sum = Solution().addPolynomial(poly1, poly2)
        ptr = sum
        while ptr is not None:
            print(str(ptr.coef) + 'x^' + str(ptr.power), end = '')
            ptr = ptr.next
            if ptr is not None:
                print(' +', end = ' ')
        print()
            
# Contributed by: Sagar Gupta

#} Driver Code Ends
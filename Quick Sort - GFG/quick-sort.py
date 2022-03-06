#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if(low<high):
            l = self.partition(arr,low,high)
            self.quickSort(arr,low,l-1)
            self.quickSort(arr,l+1,high)
        
    
    def partition(self,array,start,end):
        # code here
        # Initializing pivot's index to start
        pivot_index = start
        pivot = array[pivot_index]
         
        # This loop runs till start pointer crosses
        # end pointer, and when it does we swap the
        # pivot with element on end pointer
        while start < end:
             
            # Increment the start pointer till it finds an
            # element greater than  pivot
            while start < len(array) and array[start] <= pivot:
                start += 1
                 
            # Decrement the end pointer till it finds an
            # element less than pivot
            while array[end] > pivot:
                end -= 1
             
            # If start and end have not crossed each other,
            # swap the numbers on start and end
            if(start < end):
                array[start], array[end] = array[end], array[start]
         
        # Swap pivot element with element on end pointer.
        # This puts pivot on its correct sorted place.
        array[end], array[pivot_index] = array[pivot_index], array[end]
        
        # Returning end pointer to divide the array into 2
        return end
        
        
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
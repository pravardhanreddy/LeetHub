from collections import Counter
class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def minWindow(self, A, B):
        B = Counter(B) # Count of elements in B
        blen = len(B) # Stores how many more characters need to be satisfied
        mins = '' # The answer 
        minl = len(A) + 1 # Initialize the length of the ans
        l = 0
        for i in range(len(A)): # Iterate over each character in the string
            if A[i] in B:
                B[A[i]] -= 1
                if B[A[i]] == 0: # Requirement decreases by one
                    blen -= 1 
                while blen == 0: # Requirement is satisfied
                    if i+1-l < minl: # Check if optimal
                        mins = A[l:i+1]
                        minl = i+1-l
                    if A[l] in B:
                        B[A[l]] += 1
                        if B[A[l]] == 1: # Requirement increased
                            blen = 1
                    l += 1 # Try to keep breaking the Requirement

        return mins
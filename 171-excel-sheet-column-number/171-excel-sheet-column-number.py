class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
             
        s = 0
        
        for a in columnTitle:
            s = s * 26 + ord(a) - ord("A") + 1
            
        return s
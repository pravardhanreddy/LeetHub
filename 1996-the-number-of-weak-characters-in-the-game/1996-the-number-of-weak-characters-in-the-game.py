class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort()
        maxa = properties[-1][0]
        maxdyet = properties[-1][1]
        maxd = maxdyet
        ans = 0
        for i in range(len(properties)-2, -1, -1):
            
            
            if properties[i][0] < properties[i+1][0]:
                maxd = maxdyet
                maxdyet = max(maxdyet, properties[i][1])
            
            if properties[i][0] < maxa and properties[i][1] < maxd:
                ans += 1
        return ans
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        sub = arr[1] - arr[0]
        res = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] < sub:
                sub = arr[i+1] - arr[i]
                res = [[arr[i], arr[i+1]]]
            elif arr[i+1] - arr[i] == sub:
                res.append([arr[i], arr[i+1]])
        return res
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        rightside = -1
        res = [0] * len(arr)
        
        for i in range(len(arr)-1, -1, -1):
            
            res[i] = rightside
            rightside = max(rightside, arr[i])
        
        return res
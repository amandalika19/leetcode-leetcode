class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1
    
        for k,v in d.items():
            if v >= 2:
                return True
        
        return False
            

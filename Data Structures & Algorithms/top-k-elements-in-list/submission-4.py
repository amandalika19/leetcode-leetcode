class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for n in nums:

            d[n] = d.get(n, 0) + 1
        
        sortedDict = sorted(d.items(), key=lambda x:x[1], reverse=True)

        res = []
        for key, freq in sortedDict[:k]:
            res.append(key)
            
        return res

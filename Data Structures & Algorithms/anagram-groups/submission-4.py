class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}

        for s in strs:
            temp = tuple(sorted(s))

            if temp not in d:
                d[temp] = []
            d[temp].append(s)
        
        return list(d.values())
       
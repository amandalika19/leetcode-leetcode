class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dT = {}
        dS = {}

        for c in s:
            dS[c] = dS.get(c, 0) + 1

        for c in t:
            dT[c] = dT.get(c, 0) + 1
        
        return dT == dS
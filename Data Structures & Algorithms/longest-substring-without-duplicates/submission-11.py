class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        res = 0
        lenS = len(s)
        sset = set()

        for r in range(lenS):

            while s[r] in sset:
                sset.remove(s[l])
                l += 1
            sset.add(s[r])

            res = max(res, r - l + 1)
        
        return res
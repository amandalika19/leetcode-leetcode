class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        c = {}
        l = 0
        freq = 0

        for r in range(len(s)):
            c[s[r]] = c.get(s[r], 0) + 1
            freq = max(freq, c[s[r]])

            if (r - l + 1) - freq > k:
                c[s[l]] -= 1
                l += 1
            
        return r - l + 1
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s) - 1

        while l < r:

            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                skipR = s[l : r]
                skipL = s[l + 1: r + 1]

                if skipL == skipL[::-1] or skipR == skipR[::-1]:
                    return True
                else:
                    return False
        
        return True
        

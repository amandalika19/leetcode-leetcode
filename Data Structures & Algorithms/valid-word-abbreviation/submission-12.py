class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = j = 0
        lw = len(word)
        la = len(abbr)

        while i < lw and j < la:

            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0' or abbr[j].isalpha():
                return False
            else:
                sublen = 0
                while j < la and abbr[j].isdigit(): 
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen
    
        return i == lw and j == la
            





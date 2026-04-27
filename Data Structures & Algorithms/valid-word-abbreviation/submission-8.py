class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        wordL = len(word)
        abbrL = len(abbr)
        i = j = 0

        while i < wordL and j < abbrL:

            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0' or abbr[j].isalpha():
                return False
            else:
                sublen = 0
                while j < abbrL and abbr[j].isdigit():
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen
        
        return i == wordL and j == abbrL

        
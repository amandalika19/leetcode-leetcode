class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = j = 0
        wordl, abbrl = len(word), len(abbr)

        while i < wordl and j < abbrl:

            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0' or abbr[j].isalpha():
                return False
            else:
                sublen = 0
                while j < abbrl and abbr[j].isdigit():
                    sublen = sublen * 10 + int(abbr[j])
                    j += 1
                i += sublen
        
        return i == wordl and j == abbrl
                




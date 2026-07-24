class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        wordl, abbrl = len(word), len(abbr)
        i, j = 0, 0
        while i < wordl and j < abbrl:

            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0' or abbr[j].isalpha():
                return False
            else:

                subl = 0
                while j < abbrl and abbr[j].isdigit():
                    subl = subl * 10 + int(abbr[j])
                    j += 1
                i += subl
        
        return i == wordl and j == abbrl
            
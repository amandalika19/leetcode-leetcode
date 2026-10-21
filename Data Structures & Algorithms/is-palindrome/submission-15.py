class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        news = ""

        for c in s:
            if c.isalnum():
                news += c.lower()
        
        print(news)
        l, r = 0, len(news) - 1

        while l < r:

            if news[l] != news[r]:
                return False
            l += 1
            r -= 1
        
        return True

                
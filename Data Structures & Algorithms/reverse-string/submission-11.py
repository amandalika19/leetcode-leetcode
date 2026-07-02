class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        neet  - n = 3

        temp =
        """
        
        n = len(s) - 1

        for i in range(0, (n + 1) // 2):

            temp = s[i]
            s[i] = s[n - i]
            s[n - i] = temp
        
        return s
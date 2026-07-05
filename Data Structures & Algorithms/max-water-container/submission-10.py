class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l, r = 0, len(heights) - 1
        maxC = 0

        while l < r:

            currC = min(heights[l], heights[r]) * (r - l)
            maxC = max(currC, maxC)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxC 

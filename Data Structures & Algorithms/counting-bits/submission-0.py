class Solution:
    def countBits(self, n: int) -> List[int]:
        
        arr = []

        for num in range(0, n+1):
            ones = 0
            for i in range(32):
                if num & (1 << i):
                    ones += 1
            arr.append(ones)
        
        return arr
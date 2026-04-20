class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inc = defaultdict(int) # d is trusted
        out = defaultdict(int) # s trusts

        for s, d in trust:
            inc[d] += 1
            out[s] += 1
        
        for i in range(0, n + 1):
            
            if out[i] == 0 and inc[i] == n - 1:
                return i
        
        return -1
    


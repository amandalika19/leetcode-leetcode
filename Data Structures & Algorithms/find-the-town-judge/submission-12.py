class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        inc = defaultdict(int) #trust me
        out = defaultdict(int) #i trust

        for s,d in trust:
            inc[d] += 1
            out[s] += 1
        
        for i in range(0, n + 1):
            if inc[i] == n - 1 and out[i] == 0:
                return i
        
        return -1
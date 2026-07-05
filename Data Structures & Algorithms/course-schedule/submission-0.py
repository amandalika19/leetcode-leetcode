class Solution:
    def canFinish(self, numC: int, prereqs: List[List[int]]) -> bool:
        
        indegree = [0] * numC
        adj = [[] for i in range(numC)]
        for s, d in prereqs:
            indegree[d] += 1
            adj[s].append(d)
        
        q = collections.deque()
        for n in range(numC):
            if indegree[n] == 0:
                q.append(n)
            
        f = 0
        while q:
            n = q.popleft()
            f += 1
            for nei in adj[n]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return f == numC

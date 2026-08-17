class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for s,d in prerequisites:
            indegree[d] += 1
            adj[s].append(d)
        
        q = collections.deque()
        for n in range(numCourses):
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
        
        return f == numCourses
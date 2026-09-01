class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses

        
        
        # DFS + adjaceny list
        # preMap = {i: [] for i in range(numCourses)}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)
        
        # visitSet = set()
        # def dfs(crs):
        #     if crs in visitSet:
        #         return False
        #     if preMap[crs] == []:
        #         return True
            
        #     visitSet.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre):
        #             return False
        #     visitSet.remove(crs)
        #     preMap[crs] = []
        #     return True
        
        # for crs in range(numCourses):
        #     if not dfs(crs): return False
        # return True
    
    
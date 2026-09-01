class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        par = [i for i in range(N + 1)]
        rank = [1] * (N+1)

        def find(n):
            while n != par[n]:
                par[n] = par[par[n]] # path compression
                n = par[n]
            return n

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if (r in range(rows) and c in range(cols) and grid[r][c] == 0 
                    and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))
        
        level = 1
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < cols and 
                        grid[nr][nc] == 2147483647 and (nr, nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
                        grid[nr][nc] = level
            level += 1
                    

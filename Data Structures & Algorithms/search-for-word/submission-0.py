class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or 
                word[i] != board[r][c] or
                (r, c) in visit):
                return False
            
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i+1):
                    return True
            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
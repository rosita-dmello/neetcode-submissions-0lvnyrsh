class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        time = 0
        fresh = 0
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        while q and fresh > 0:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr < 0 or nr == rows or nc < 0 or nc == cols or grid[nr][nc] != 1:
                        continue
                    q.append((nr,nc))
                    fresh -= 1
                    grid[nr][nc] = 2
            time += 1
        
        return -1 if fresh > 0 else time
            
            
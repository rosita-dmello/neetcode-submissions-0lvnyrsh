class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr, nc))

                
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == '1':
                    visited.add((r,c))
                    bfs(r,c)
                    islands += 1
        return islands                
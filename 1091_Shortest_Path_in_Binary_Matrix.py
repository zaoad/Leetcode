from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        node = (0, 0)
        dist = [[-1 for i in range(n)] for j in range(n)]
        q = deque()
        q.append(node)
        dist[0][0] = 1
        # print(dist[0][0], dist[1][0])
        while len(q) != 0:
            (x, y) = q.popleft()

            for d_x , d_y in dir:
                t_x = x+d_x
                t_y = y+d_y
                if t_x < 0 or t_x>=n or t_y <0 or t_y>=n:
                    continue
                if grid[t_x][t_y] == 0:
                    q.append((t_x, t_y))
                    dist[t_x][t_y] = dist[x][y]+1
                    grid[t_x][t_y] =1
                    print(t_x, t_y, dist)
        print(dist)
        return dist[n-1][n-1]

s = Solution()
ans = s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]]
)
print(ans)

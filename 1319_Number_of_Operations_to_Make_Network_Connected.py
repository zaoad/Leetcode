from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        vis = [False for _ in range(n)]
        edges = [[] for _ in range(n)]

        def dfs(node):
            if vis[node]:
                return
            vis[node] = True
            for i in edges[node]:
                dfs(i)

        for e in connections:
            u, v = e
            edges[u].append(v)
            edges[v].append(u)

        s = 0
        for i in range(n):
            if not vis[i]:
                s += 1
                dfs(i)

        return s - 1


s = Solution()
n = 4
connections = [[0, 1], [0, 2], [1, 2]]
ans = s.makeConnected(n, connections)
print(ans)

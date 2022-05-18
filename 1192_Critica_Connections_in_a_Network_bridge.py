from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = dict()
        for i in range(n):
            graph[i+1] = []
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        self.t = 0
        bridge = []
        vis = set()
        parent = [0]*(n+1)
        dis, low = [0]*(n+1), [0]*(n+1)
        def bridgefind(source):
            dis[source] = self.t + 1
            low[source] = self.t + 1
            self.t += 1
            for child in graph[source]:
                if child == parent[source]:
                    continue
                if child in vis:
                    low[source] = min(low[source], dis[child])
                else:
                    vis.add(child)
                    parent[child] = source
                    bridgefind(child)
                    low[source] = min(low[child], low[source])
                    if low[child] > dis[source]:
                        bridge.append([source,child])

        bridgefind(1)
        return bridge


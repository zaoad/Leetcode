import math
from typing import List
from heapq import heappush, heappop
import math

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        edges = [[] for _ in range(n+1)]
        for l in roads:
            [s, d, w] = l
            edges[s].append((d, w))
            edges[d].append((s, w))
        h = []
        visited = set()
        distances = [math.inf for _ in range(n+1)]
        heappush(h, (math.inf, 1))
        min_value = 10000
        while len(h)>0:
            s, current = heappop(h)
            # print("a", s, current)
            visited.add(current)
            for (child, w) in edges[current]:
                if child not in visited:
                    min_value = min(min_value, w)
                    heappush(h, (min_value, child))
                    visited.add(child)

        # return distances[n]
        print(distances[n])
        print(distances)
        print(edges)
        print(min_value)


s = Solution()
s.minScore(4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]])

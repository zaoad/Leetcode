from typing import List
import heapq as hq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = dict()
        w = [[0]*n]*n
        inf = 1000000007
        dis = [inf]*n
        for i in range(n):
            graph[i] = list()
        for u, v, t in times:
            graph[u-1].append((v-1, t))
            # graph[v-1].append((u-1, t))
        my_heap = [(0,k-1)]
        dis[k-1] = 0
        while my_heap:
            t, node = hq.heappop(my_heap)
            for c, t1 in graph[node]:
                if dis[c] > dis[node]+t1:
                    dis[c] = dis[node]+t1
                    hq.heappush(my_heap, (dis[node]+t1, c))
        val = max(dis)
        print(dis, val)
        if val== inf:
            return -1
        else:
            return val


s = Solution()
s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)




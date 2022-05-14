from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.h = len(heights)
        self.dp = [[-1]*h]*h


    def dp(self,heighs, x, y, d):
        if x==self.h-1 and y == self.h-1:
            return abs(heighs[x][y]-d)
        if self.dp[x][y] != -1:
            return self.dp[x][y]
        



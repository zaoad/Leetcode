from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        my_dict = dict()
        parent = [0] * len(s)
        for i in range(len(s)):
            parent[i] = i
        groups = {}
        for [a, b] in pairs:
            p = self.union(parent, a, b)

        for i in range(len(s)):
            p = self.find_parent(parent, i)
            if p not in groups:
                groups[p] = ([], [])
            groups[p][0].append(s[i])
            groups[p][1].append(i)
        new_s = [''] * len(s)
        # print(groups)
        for k, v in groups.items():
            # print(k,v)
            v[0].sort()
            v[1].sort()
            # print(v[0], v[1])
            for i in range(len(v[1])):
                new_s[v[1][i]] = v[0][i]

        return ''.join(new_s)

    def find_parent(self, parent, i):
        # print(parent, i)
        if parent[i] == i:
            return i;
        # print('p', parent[i])
        return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        p_x = self.find_parent(parent, x)
        p_y = self.find_parent(parent, y)
        if p_x < p_y:
            parent[p_y] = p_x
            return p_x
        else:
            parent[p_x] = p_y
            return p_y


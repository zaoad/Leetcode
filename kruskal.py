# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

from collections import defaultdict


# Class to represent a graph


class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = [] # default dictionary
        self.parent = []

    # to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def findParent(self, i):
        if self.parent[i] == i:
            return i
        return self.findParent(self.parent[i])

    def union(self, x, y):
        p_x = self.findParent(x)
        p_y = self.findParent(y)
        if p_y < p_x:
            self.parent[p_x] = p_y
        else:
            self.parent[p_y] = p_x


    # The main function to construct MST using Kruskal's
    # algorithm
    def KruskalMST(self):
        result = []  # This will store the resultant MST

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0
        for p in range(self.V):
            self.parent.append(p)
        self.graph.sort(key=lambda item: item[2])
        print(self.graph)
        l = len(self.graph)
        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            print('i', i)
            u, v, w = self.graph[i]
            i = i + 1
            x = self.findParent(u)
            y = self.findParent(v)
            print(x,y)
            if x!=y:

                self.union(u,v)
                result.append([u, v, w])
                print('parent', self.parent)
                print('result', result)
                e+=1


        # Else discard the edge

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        return minimumCost

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

points = [[2,-3],[-17,-8],[13,8],[-17,-15]]
v = len(points)
g = Graph(v)
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p = points[i]
        p1 = points[j]
        g.addEdge(i, j, distance(p, p1))


# Function call
print(g.KruskalMST())
# This code is contributed by Neelam Yadav
# Driver code
# g = Graph(4)
# g.addEdge(0, 1, 10)
# g.addEdge(0, 2, 6)
# g.addEdge(0, 3, 5)
# g.addEdge(1, 3, 15)
# g.addEdge(2, 3, 4)
#
# # Function call
# print(g.KruskalMST())
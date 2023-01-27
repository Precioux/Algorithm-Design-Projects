'''
Samin Mahdipour - 9839039
Algorithm Design - HW4 -Q2
'''

class graphMaker:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    # union of two sets of x and y
    def unionSets(self, parent, rank, x, y):

        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        else:
            parent[y] = x
            rank[x] += 1

    # Finds Min Spanning Tree
    def findMinSpanTree(self):

        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:

            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.unionSets(parent, rank, x, y)

        minCost = 0
        for u, v, weight in result:
            minCost += weight
        return minCost


if __name__ == '__main__':
    s = input()
    nums = s.split(' ')
    n = int(nums[0])
    m = int(nums[1])
    graph = graphMaker(int(n))
    tot = 0
    for i in range(m):
        d = input()
        str = d.split(' ')
        startV = int(str[0])
        endV = int(str[1])
        weight = int(str[2])
        tot = tot + weight
        graph.addEdge(startV, endV, weight)

    mst = graph.findMinSpanTree()
    print(tot - mst)

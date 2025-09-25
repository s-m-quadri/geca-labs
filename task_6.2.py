# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
 
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False
def kruskal_mst(vertices, edges):
    # edges: (weight, u, v)
    edges.sort()
    dsu = DisjointSet(vertices)
    mst = []
 
    for weight, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
 
    return mst

n = int(input("enter the number of edges: "))
V = int(input("enter no of vertics: "))
list=[]

for i in range(n):
    u = int(input("enter u: "))
    v = int(input("enter v: "))
    w = int(input("enter w: "))
    list.append((u,v,w))

mst = kruskal_mst(V, list)
for u, v, w in mst:
    print(f"{u} - {v}\t{w}")


    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
 
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
 
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False  
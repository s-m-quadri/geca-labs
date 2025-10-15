def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if xroot != yroot:
        parent[yroot] = xroot

parent = [0,1,2,3]
union(parent, 0, 1)
union(parent, 1, 2)
print(find(parent, 2))
print(parent)


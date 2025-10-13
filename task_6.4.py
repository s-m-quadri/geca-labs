# Task 6.4: Find and Union Functions
# -----------------------------------
# Extend union-find with:
# 1. find(x) -> returns root parent of x.
# 2. union(x, y) -> merges sets containing x and y.

# Example:
# parent = [0,1,2,3]
# union(0,1) → parent updated
# find(1) → should return 0 after union

# Hint: Use recursion for find().
# Tip: Try multiple unions, like (0,1), (1,2).
def initialize_union_find(n):
    parent = [i for i in range(n)]
    return parent

def find(x, parent):
    if parent[x] != x:
        return find(parent[x], parent)
    return x

def union(x, y, parent):
    root_x = find(x, parent)
    root_y = find(y, parent)
    if root_x != root_y:
        parent[root_y] = root_x

n = 4
parent = initialize_union_find(n)
union(0, 1, parent)
union(1, 2, parent)
print(find(2, parent)) 
print(parent)

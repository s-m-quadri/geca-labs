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

def find(parent, x):
    """
    Find the root parent of vertex x using path compression.
    Returns the root of the set containing x.
    """
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # Path compression
    return parent[x]

def find_without_compression(parent, x):
    """
    Find the root parent without path compression (simple recursive version).
    """
    if parent[x] == x:
        return x
    return find_without_compression(parent, parent[x])

def union(parent, x, y):
    """
    Union the sets containing x and y.
    Makes the root of y's set point to the root of x's set.
    """
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        parent[root_y] = root_x
        return True  # Union performed
    return False  # Already in same set

def are_connected(parent, x, y):
    """
    Check if two vertices are in the same connected component.
    """
    return find(parent, x) == find(parent, y)

def print_union_find_state(parent, title="Union-Find State"):
    """
    Print the current state of the union-find structure.
    """
    print(f"{title}:")
    print(f"parent = {parent}")
    
    n = len(parent)
    sets = {}
    for i in range(n):
        root = find_without_compression(parent.copy(), i)
        if root not in sets:
            sets[root] = []
        sets[root].append(i)
    
    print("Connected components:")
    for root, members in sorted(sets.items()):
        print(f"  Set {root}: {members}")

parent = [0, 1, 2, 3]
print("Test Case 1 - Initial state:")
print_union_find_state(parent, "Initial")

print(f"\nBefore union(0,1):")
print(f"find(0) = {find(parent.copy(), 0)}")
print(f"find(1) = {find(parent.copy(), 1)}")
print(f"Are 0 and 1 connected? {are_connected(parent, 0, 1)}")

union_result = union(parent, 0, 1)
print(f"\nAfter union(0,1) - Union performed: {union_result}")
print_union_find_state(parent, "After union(0,1)")

print(f"find(0) = {find(parent.copy(), 0)}")
print(f"find(1) = {find(parent.copy(), 1)}")
print(f"Are 0 and 1 connected? {are_connected(parent, 0, 1)}")

print("\n" + "="*50)

print("Test Case 2 - Multiple unions:")
parent2 = [0, 1, 2, 3, 4]
print_union_find_state(parent2, "Initial state")

operations = [(0, 1), (1, 2), (3, 4)]
for x, y in operations:
    print(f"\nPerforming union({x}, {y}):")
    union_performed = union(parent2, x, y)
    print(f"Union performed: {union_performed}")
    print_union_find_state(parent2, f"After union({x},{y})")

print("\n" + "="*50)

print("Test Case 3 - Cycle detection:")
parent3 = [0, 1, 2, 3]
edges_to_test = [(0, 1), (1, 2), (2, 3), (3, 0)]

print("Testing edges for cycle detection:")
for u, v in edges_to_test:
    if are_connected(parent3, u, v):
        print(f"Edge ({u}, {v}) would create a cycle!")
        break
    else:
        print(f"Edge ({u}, {v}) is safe to add")
        union(parent3, u, v)
        print_union_find_state(parent3, f"After adding ({u}, {v})")
        print()

print("Final connected components:")
print_union_find_state(parent3, "Final state")

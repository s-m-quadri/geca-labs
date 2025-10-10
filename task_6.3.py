# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

# Hint: Use list comprehension.
# Tip: No path compression or union by rank yet.

def initialize_union_find(n):
    """
    Initialize union-find data structure for n vertices.
    Each vertex is initially its own parent (separate set).
    """
    return [i for i in range(n)]

def initialize_union_find_alternative(n):
    """
    Alternative way to initialize using list() and range().
    """
    return list(range(n))

def print_union_find_state(parent):
    """
    Print the current state of the union-find structure.
    """
    n = len(parent)
    print(f"Union-Find for {n} vertices:")
    print(f"parent = {parent}")
    
    print("Each vertex and its parent:")
    for i in range(n):
        print(f"  vertex {i} -> parent {parent[i]}")
    
    sets = {}
    for i in range(n):
        if parent[i] not in sets:
            sets[parent[i]] = []
        sets[parent[i]].append(i)
    
    print("Current sets (each vertex is in its own set initially):")
    for root, members in sets.items():
        if root in members:
            print(f"  Set {root}: {members}")

n1 = 5
parent1 = initialize_union_find(n1)
print("Test Case 1:")
print_union_find_state(parent1)

print("\n" + "="*50)

n2 = 8
parent2 = initialize_union_find_alternative(n2)
print("Test Case 2 - Alternative method:")
print_union_find_state(parent2)

print("\n" + "="*50)

print("Test Case 3 - Verification:")
n3 = 10
parent3 = initialize_union_find(n3)
print(f"Created parent array for {n3} vertices: {parent3}")
print(f"Expected: {list(range(n3))}")
print(f"Arrays match: {parent3 == list(range(n3))}")

print("\nProperty verification:")
print(f"All vertices are self-parents: {all(parent3[i] == i for i in range(n3))}")
print(f"Length matches vertex count: {len(parent3) == n3}")

print("\nTest Case 4 - Edge cases:")
parent_empty = initialize_union_find(0)
print(f"Empty graph (0 vertices): {parent_empty}")

parent_single = initialize_union_find(1)
print(f"Single vertex: {parent_single}")

parent_pair = initialize_union_find(2)
print(f"Two vertices: {parent_pair}")

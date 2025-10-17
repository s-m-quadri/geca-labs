# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.

def sort_edges_by_weight(edges):
    return sorted(edges, key=lambda x: x[2])

n = int(input("Enter number of edges: "))
edges = []
for i in range(n):
    u = int(input(f"Enter starting vertex of edge {i+1}: "))
    v = int(input(f"Enter ending vertex of edge {i+1}: "))
    w = int(input(f"Enter weight of edge {i+1}: "))
    edges.append((u, v, w))

sorted_edges = sort_edges_by_weight(edges)
print("Edges sorted by weight:", sorted_edges)

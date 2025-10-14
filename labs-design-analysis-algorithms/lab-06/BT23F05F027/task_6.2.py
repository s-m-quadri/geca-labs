# Task 6.2: Sorting Edges
# ------------------------
# Write a function that sorts edges by their weight.
# Use Python's built-in sorted().

# Example:
# Input: [(0,1,4), (0,2,3), (1,2,1)]
# Expected Output: [(1,2,1), (0,2,3), (0,1,4)]

# Hint: Sort using key = lambda x: x[2]
# Tip: Test with 5-6 edges to check order.

def extract_vertices(edges):
    vertices = set()
    for u, v, _ in edges:
        vertices.add(u)
        vertices.add(v)
    return vertices

# Example usage
vertices = extract_vertices(edges)
print("Vertices:", vertices)
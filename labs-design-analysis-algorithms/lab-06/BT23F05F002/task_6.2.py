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
    """
    Sort edges by their weight in ascending order.
    Each edge is a tuple (u, v, w) where w is the weight.
    """
    return sorted(edges, key=lambda x: x[2])

def sort_edges_by_weight_inplace(edges):
    """
    Sort edges in-place by their weight.
    """
    edges.sort(key=lambda x: x[2])
    return edges

def print_edges_comparison(original, sorted_edges):
    """
    Print original and sorted edges for comparison.
    """
    print("Original edges:")
    for i, (u, v, w) in enumerate(original):
        print(f"  {i}: ({u}, {v}) weight={w}")
    
    print("\nSorted edges (by weight):")
    for i, (u, v, w) in enumerate(sorted_edges):
        print(f"  {i}: ({u}, {v}) weight={w}")
    
    weights = [w for u, v, w in sorted_edges]
    print(f"\nWeights in order: {weights}")
    print(f"Is sorted: {weights == sorted(weights)}")

edges1 = [(0, 1, 4), (0, 2, 3), (1, 2, 1)]
sorted_edges1 = sort_edges_by_weight(edges1)

print("Test Case 1:")
print_edges_comparison(edges1, sorted_edges1)

print("\n" + "="*50)

edges2 = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
sorted_edges2 = sort_edges_by_weight(edges2)

print("Test Case 2 - 5 edges:")
print_edges_comparison(edges2, sorted_edges2)

print("\n" + "="*50)

edges3 = [
    (0, 1, 2), (0, 3, 6), (1, 2, 3), (1, 3, 8), 
    (1, 4, 5), (2, 4, 7), (3, 4, 9), (2, 5, 1)
]
sorted_edges3 = sort_edges_by_weight(edges3)

print("Test Case 3 - 8 edges:")
print_edges_comparison(edges3, sorted_edges3)

print("\n" + "="*50)

print("Test Case 4 - In-place sorting:")
edges4 = [(3, 4, 12), (1, 2, 8), (0, 1, 5), (2, 3, 3)]
print(f"Before in-place sort: {edges4}")
sort_edges_by_weight_inplace(edges4)
print(f"After in-place sort:  {edges4}")

print("\nTest Case 5 - Edges with same weights:")
edges5 = [(0, 1, 5), (1, 2, 3), (2, 3, 5), (3, 4, 3), (4, 0, 1)]
sorted_edges5 = sort_edges_by_weight(edges5)
print(f"Original: {edges5}")
print(f"Sorted:   {sorted_edges5}")
print("Note: Edges with same weights maintain their relative order (stable sort)")

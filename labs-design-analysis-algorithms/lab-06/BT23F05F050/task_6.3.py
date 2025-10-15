def initialize_union_find(V):
    # Each vertex is its own parent initially
    parent = [i for i in range(V)]
    return parent

# Example
V = 5
parent = initialize_union_find(V)
print("Initial parent array:", parent)
# Output: [0, 1, 2, 3, 4]

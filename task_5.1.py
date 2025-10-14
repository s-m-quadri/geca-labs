def initialize_prim(V):
    """
    Initialize key, parent, and mstSet arrays for Prim's algorithm.

    V: number of vertices
    Returns: key, parent, mstSet
    """
    key = [float('inf')] * V      # ∞ for all vertices
    parent = [-1] * V             # -1 indicates no parent yet
    mstSet = [False] * V          # False indicates vertex not yet included in MST
    return key, parent, mstSet

# Example usage
V = 4
key, parent, mstSet = initialize_prim(V)

print("key:", key)
print("parent:", parent)
print("mstSet:", mstSet)

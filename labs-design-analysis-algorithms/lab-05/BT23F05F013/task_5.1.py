"""
Background:
Prim's algorithm finds a Minimum Spanning Tree (MST) in a weighted graph.

Task:
Write a function that initializes key[], parent[], mstSet[] arrays for a graph with V vertices.

Instruction:
- Use Python lists.
- Do not implement the full MST yet.

Tip:
Focus only on initialization. Use ∞ for key values and -1 for parent.

Test case:
V = 4
# Expected:
# key = [∞, ∞, ∞, ∞]
# parent = [-1, -1, -1, -1]
# mstSet = [False, False, False, False]
"""

def initialize_prim_arrays(V):
    """
    Initialize arrays for Prim's algorithm.
    
    Args:
        V: Number of vertices in the graph
    
    Returns:
        tuple: (key, parent, mstSet) arrays
    """
    # Initialize key values to infinity (using float('inf'))
    key = [float('inf')] * V
    
    # Initialize parent array to -1 (no parent initially)
    parent = [-1] * V
    
    # Initialize mstSet to False (no vertex in MST initially)
    mstSet = [False] * V
    
    return key, parent, mstSet

# Test the function
if __name__ == "__main__":
    V = 4
    key, parent, mstSet = initialize_prim_arrays(V)
    
    print(f"key = {key}")
    print(f"parent = {parent}")
    print(f"mstSet = {mstSet}")
    
    # Verify the initialization
    assert len(key) == V
    assert len(parent) == V
    assert len(mstSet) == V
    assert all(k == float('inf') for k in key)
    assert all(p == -1 for p in parent)
    assert all(m == False for m in mstSet)
    
    
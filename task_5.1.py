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

def initialize_prim(V):
    """
    Initialize the arrays needed for Prim's algorithm.
    
    Args:
        V: Number of vertices in the graph
    
    Returns:
        tuple: (key, parent, mstSet)
    """
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    
    return key, parent, mstSet


# Test case
if __name__ == "__main__":
    V = 4
    key, parent, mstSet = initialize_prim(V)
    
    print(f"key = {key}")
    print(f"parent = {parent}")
    print(f"mstSet = {mstSet}")
    
    # Verify
    print("\nVerification:")
    print(f"All keys are infinity: {all(k == float('inf') for k in key)}")
    print(f"All parents are -1: {all(p == -1 for p in parent)}")
    print(f"All mstSet are False: {all(not m for m in mstSet)}")

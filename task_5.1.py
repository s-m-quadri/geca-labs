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
    # Initialize key values as infinity for all vertices
    key = [float('inf')] * V
    
    # Initialize parent array with -1 (no parent initially)
    parent = [-1] * V
    
    # Initialize mstSet to track vertices included in MST
    mstSet = [False] * V
    
    return key, parent, mstSet

# Test the function
if __name__ == "__main__":
    V = 4
    key, parent, mstSet = initialize_prim_arrays(V)
    
    print(f"Number of vertices: {V}")
    print(f"key array: {key}")
    print(f"parent array: {parent}")
    print(f"mstSet array: {mstSet}")
    
    # Verify the initialization
    print("\nVerification:")
    print(f"All keys are infinity: {all(k == float('inf') for k in key)}")
    print(f"All parents are -1: {all(p == -1 for p in parent)}")
    print(f"All mstSet values are False: {all(not mst for mst in mstSet)}")
    
    # Test with different sizes
    print(f"\nTesting with V = 6:")
    key6, parent6, mstSet6 = initialize_prim_arrays(6)
    print(f"key array length: {len(key6)}")
    print(f"parent array length: {len(parent6)}")
    print(f"mstSet array length: {len(mstSet6)}")

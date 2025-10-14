def initialize_prim(V):
    """
    Initialize key[], parent[], and mstSet[] for Prim's algorithm.

    Parameters:
    V : int
        Number of vertices in the graph.

    Returns:
    key : list
        Minimum edge weight to include each vertex in MST, initialized to infinity.
    parent : list
        Parent of each vertex in MST, initialized to -1.
    mstSet : list
        Boolean array to track vertices included in MST, initialized to False.
    """
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    return key, parent, mstSet

# Test case
V = 4
key, parent, mstSet = initialize_prim(V)
print("key =", key)
print("parent =", parent)
print("mstSet =", mstSet)

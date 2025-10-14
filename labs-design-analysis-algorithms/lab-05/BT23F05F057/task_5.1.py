def initialize_prim(V):
    # Use float('inf') to represent infinity
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    return key, parent, mstSet


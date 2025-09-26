def initialize_prim(V):
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    return key, parent, mstSet

V = 4
key, parent, mstSet = initialize_prim(V)
print("key =", key)
print("parent =", parent)
print("mstSet =", mstSet)

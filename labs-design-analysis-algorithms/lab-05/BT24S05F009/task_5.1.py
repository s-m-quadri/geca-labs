def initialize_prim_arrays(V):
    key = [float('inf')] * V
    parent = [-1] * V
    mstSet = [False] * V
    return key, parent, mstSet

# Example usage and test
if __name__ == "__main__":
    V = 4
    key, parent, mstSet = initialize_prim_arrays(V)
    print("key =", key)
    print("parent =", parent)
    print("mstSet =", mstSet)

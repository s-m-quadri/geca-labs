def initialize_union_find(V):
    """
    Initializes parent array for Union-Find.
    Each vertex is its own parent initially.
    """
    parent = [i for i in range(V)]
    return parent

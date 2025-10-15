def initialize_union_find(V):
    parent = [i for i in range(V)]
    return parent

V = 5
parent = initialize_union_find(V)
print(parent)

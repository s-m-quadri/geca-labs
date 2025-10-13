def min_key_vertex(key, mstSet):
    min_val = float('inf')
    min_index = -1

    for v in range(len(key)):
        if not mstSet[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index

def min_key_vertex(key, mstSet):
    min_val = float('inf')
    min_index = -1
    for i in range(len(key)):
        if not mstSet[i] and key[i] < min_val:
            min_val = key[i]
            min_index = i
    return min_index

key = [0, 2, 3]
mstSet = [True, False, False]
print(min_key_vertex(key, mstSet))

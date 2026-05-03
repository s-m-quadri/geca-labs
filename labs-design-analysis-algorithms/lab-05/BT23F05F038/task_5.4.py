"""
Background:
Prim's algorithm repeats selection and update steps to build MST.

Task:
Combine selection of min-key vertex and neighbor updates in one iteration.

Instruction:

Tip:
Test on small 3-4 vertex graphs to check updates.

Test case:
graph = [
 [0, 1, 4],
 [1, 0, 2],
 [4, 2, 0]
]
key = [0, ∞, ∞]
mstSet = [True, False, False]
parent = [-1, -1, -1]
# Expected after iteration:
# key = [0, 1, 2]
# parent = [-1, 0, 1]
"""

def prim_iteration(graph, key, parent, mstSet):
	# Find min-key vertex not in MST
	min_val = float('inf')
	u = -1
	for i in range(len(key)):
		if not mstSet[i] and key[i] < min_val:
			min_val = key[i]
			u = i
	if u == -1:
		return  # No vertex to process
	mstSet[u] = True
	# Update keys and parents for neighbors
	for v in range(len(graph)):
		if graph[u][v] != 0 and not mstSet[v] and graph[u][v] < key[v]:
			key[v] = graph[u][v]
			parent[v] = u

# Test case
if __name__ == "__main__":
	inf = float('inf')
	graph = [
		[0, 1, 4],
		[1, 0, 2],
		[4, 2, 0]
	]
	key = [0, inf, inf]
	mstSet = [True, False, False]
	parent = [-1, -1, -1]
	prim_iteration(graph, key, parent, mstSet)
	print("key =", key)
	print("parent =", parent)

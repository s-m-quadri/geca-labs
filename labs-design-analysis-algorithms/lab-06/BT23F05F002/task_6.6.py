# Task 6.6: Challenge - Visualize MST
# -------------------------------------
# Extend Kruskal's algorithm:
# 1. Input edges and build MST.
# 2. Print MST edges in adjacency list format.
# 3. (Optional for extra) Use networkx + matplotlibprint("\n✨ MST Visualization Complete! ✨") Example:
# MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# Expected adjacency list:
# 0: [1, 3]
# 1: [0]
# 2: [3]
# 3: [0, 2]

# Hint: Use dictionary for adjacency list.
# Tip: Visualization part is optional, but fun for testing.

def find(parent, x):
    """Find root of x with path compression."""
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    """Union by rank for better performance."""
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    return False

def kruskals_mst_with_visualization(vertices, edges, show_steps=True):
    """
    Kruskal's algorithm with MST visualization and adjacency list representation.
    
    Args:
        vertices: number of vertices in graph
        edges: list of tuples (u, v, weight)
        show_steps: whether to show algorithm steps
    
    Returns:
        tuple: (mst_edges, total_weight, adjacency_list)
    """
    mst_edges = []
    total_weight = 0
    
    parent = list(range(vertices))
    rank = [0] * vertices
    
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    if show_steps:
        print("🌳 Kruskal's MST Algorithm with Visualization")
        print("=" * 50)
        print(f"Input: {vertices} vertices, {len(edges)} edges")
        print(f"Sorted edges: {sorted_edges}")
        print()
    
    for i, (u, v, weight) in enumerate(sorted_edges):
        if show_steps:
            print(f"Step {i+1}: Considering edge ({u}, {v}) with weight {weight}")
        
        if find(parent, u) != find(parent, v):
            if union(parent, rank, u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight
                if show_steps:
                    print(f"  ✅ Added to MST. Total weight: {total_weight}")
                
                if len(mst_edges) == vertices - 1:
                    if show_steps:
                        print(f"  🎉 MST complete with {vertices-1} edges!")
                    break
        else:
            if show_steps:
                print(f"  ❌ Rejected (would create cycle)")
        
        if show_steps:
            print()
    
    adjacency_list = create_adjacency_list(mst_edges, vertices)
    
    return mst_edges, total_weight, adjacency_list

def create_adjacency_list(mst_edges, vertices):
    """
    Convert MST edges to adjacency list representation.
    
    Args:
        mst_edges: list of MST edges (u, v, weight)
        vertices: number of vertices
    
    Returns:
        dict: adjacency list representation
    """
    adj_list = {i: [] for i in range(vertices)}
    
    for u, v, weight in mst_edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    for vertex in adj_list:
        adj_list[vertex].sort()
    
    return adj_list

def print_adjacency_list(adj_list, title="MST Adjacency List"):
    """Print adjacency list in formatted way."""
    print(f"\n{title}:")
    print("-" * len(title))
    for vertex, neighbors in sorted(adj_list.items()):
        print(f"{vertex}: {neighbors}")

def create_mst_matrix(mst_edges, vertices):
    """Create adjacency matrix representation of MST."""
    matrix = [[0] * vertices for _ in range(vertices)]
    
    for u, v, weight in mst_edges:
        matrix[u][v] = weight
        matrix[v][u] = weight
    
    return matrix

def print_mst_matrix(matrix, title="MST Adjacency Matrix"):
    """Print MST as adjacency matrix."""
    print(f"\n{title}:")
    print("-" * len(title))
    vertices = len(matrix)
    
    print("   ", end="")
    for i in range(vertices):
        print(f"{i:4}", end="")
    print()
    
    for i in range(vertices):
        print(f"{i}: ", end="")
        for j in range(vertices):
            print(f"{matrix[i][j]:4}", end="")
        print()

def analyze_mst_properties(mst_edges, total_weight, vertices):
    """Analyze and display MST properties."""
    print(f"\n🔍 MST Analysis:")
    print("-" * 20)
    print(f"• Vertices: {vertices}")
    print(f"• MST Edges: {len(mst_edges)}")
    print(f"• Expected edges for spanning tree: {vertices - 1}")
    print(f"• Total Weight: {total_weight}")
    print(f"• Average edge weight: {total_weight / len(mst_edges):.2f}" if mst_edges else "N/A")
    
    if len(mst_edges) == vertices - 1:
        print("✅ Valid spanning tree (correct number of edges)")
    else:
        print("❌ Not a valid spanning tree (incorrect number of edges)")

def draw_simple_mst_text(mst_edges, vertices):
    """Create a simple text-based visualization of the MST."""
    print(f"\n🎨 Simple MST Visualization:")
    print("-" * 30)
    
    print("Edges in MST:")
    for i, (u, v, weight) in enumerate(mst_edges, 1):
        print(f"  {i}. Vertex {u} ←--({weight})--→ Vertex {v}")
    
    print(f"\nTree structure (vertices: {list(range(vertices))}):")
    adj_list = create_adjacency_list(mst_edges, vertices)
    
    visited = set()
    def dfs_print(node, depth=0, parent=None):
        if node in visited:
            return
        visited.add(node)
        
        indent = "  " * depth
        if parent is not None:
            edge_weight = next((w for u, v, w in mst_edges if (u == parent and v == node) or (u == node and v == parent)), "?")
            print(f"{indent}└─ {node} (weight: {edge_weight})")
        else:
            print(f"{indent}{node} (root)")
        
        for neighbor in adj_list[node]:
            if neighbor != parent:
                dfs_print(neighbor, depth + 1, node)
    
    if vertices > 0:
        dfs_print(0)

print("🧪 Test Case 1 - Given example:")
edges1 = [(0,1,10), (0,2,6), (0,3,5), (1,3,15), (2,3,4)]
mst_edges1, total_weight1, adj_list1 = kruskals_mst_with_visualization(4, edges1)

print_adjacency_list(adj_list1, "Expected: 0:[1,3], 1:[0], 2:[3], 3:[0,2]")
mst_matrix1 = create_mst_matrix(mst_edges1, 4)
print_mst_matrix(mst_matrix1)
analyze_mst_properties(mst_edges1, total_weight1, 4)
draw_simple_mst_text(mst_edges1, 4)

print("\n" + "="*60)

print("🧪 Test Case 2 - Larger graph:")
edges2 = [
    (0,1,4), (0,7,8), (1,2,8), (1,7,11), (2,3,7), (2,8,2), (2,5,4),
    (3,4,9), (3,5,14), (4,5,10), (5,6,2), (6,7,1), (6,8,6), (7,8,7)
]

mst_edges2, total_weight2, adj_list2 = kruskals_mst_with_visualization(9, edges2, show_steps=False)

print(f"🌳 MST Result: {len(mst_edges2)} edges, total weight: {total_weight2}")
print_adjacency_list(adj_list2)
analyze_mst_properties(mst_edges2, total_weight2, 9)
draw_simple_mst_text(mst_edges2, 9)

print("\n" + "="*60)

print("🧪 Test Case 3 - Disconnected graph:")
edges3 = [(0,1,1), (1,2,2), (3,4,3)]
mst_edges3, total_weight3, adj_list3 = kruskals_mst_with_visualization(5, edges3, show_steps=False)

print(f"🌳 MST Result: {len(mst_edges3)} edges, total weight: {total_weight3}")
print_adjacency_list(adj_list3, "Disconnected Graph - Multiple Components")
analyze_mst_properties(mst_edges3, total_weight3, 5)

if len(mst_edges3) < 4:
    print("⚠️  Note: This is a forest (multiple trees) since the graph is disconnected")

print("\n" + "="*60)

print("🎯 Verification for Test Case 1:")
expected_adj = {0: [1, 3], 1: [0], 2: [3], 3: [0, 2]}
print(f"Expected adjacency list: {expected_adj}")
print(f"Actual adjacency list:   {adj_list1}")
print(f"Match: {adj_list1 == expected_adj}")
print(f"Expected weight: 19, Actual weight: {total_weight1}, Match: {total_weight1 == 19}")

print("\n✨ MST Visualization Complete! ✨")
#enge - Visualize MST
# -------------------------------------
# Extend Kruskal’s algorithm:
# 1. Input edges and build MST.
# 2. Print MST edges in adjacency list format.
# 3. (Optional for extra) Use networkx + matplotlib to plot MST.

# Example:
# MST edges: [(2,3,4), (0,3,5), (0,1,10)]
# Expected adjacency list:
# 0: [1, 3]
# 1: [0]
# 2: [3]
# 3: [0, 2]

# Hint: Use dictionary for adjacency list.
# Tip: Visualization part is optional, but fun for testing.

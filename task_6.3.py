# Task 6.3: Union-Find Data Structure (Basics)
# ---------------------------------------------
# Implement a simple parent[] array for union-find.
# Only create parent[] such that parent[i] = i initially.

# Example:
# Input: 5 vertices
# Expected parent: [0, 1, 2, 3, 4]

class UnionFind:
    """
    A simple Union-Find data structure implementation.
    Initially, each vertex is its own parent.
    """
    def __init__(self, V):
        """Initialize parent array for V vertices"""
        self.parent = [i for i in range(V)]
        self.size = V
    
    def get_parent_array(self):
        """Return the current parent array"""
        return self.parent
    
    def validate_vertex(self, v):
        """Validate if vertex v is within bounds"""
        if not 0 <= v < self.size:
            raise ValueError(f"Vertex {v} is out of bounds [0, {self.size-1}]")

def initialize_union_find(V):
    """
    Initialize parent array for Union-Find.
    
    Args:
        V: Number of vertices
        
    Returns:
        List where each element is initially its own index
    """
    if V < 0:
        raise ValueError("Number of vertices must be non-negative")
    return [i for i in range(V)]

def print_sets(parent):
    """Helper function to print the current sets"""
    sets = {}
    for i in range(len(parent)):
        if parent[i] not in sets:
            sets[parent[i]] = []
        sets[parent[i]].append(i)
    
    print("\nCurrent sets:")
    for parent_id, members in sets.items():
        print(f"Set with parent {parent_id}: {members}")

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic initialization
    print("Test 1: Basic initialization with 5 vertices")
    V1 = 5
    parent1 = initialize_union_find(V1)
    print(f"Parent array: {parent1}")
    print(f"Verification: {parent1 == [0, 1, 2, 3, 4]}")
    print_sets(parent1)
    
    # Test case 2: Single vertex
    print("\nTest 2: Single vertex")
    V2 = 1
    parent2 = initialize_union_find(V2)
    print(f"Parent array: {parent2}")
    print(f"Verification: {parent2 == [0]}")
    print_sets(parent2)
    
    # Test case 3: Using UnionFind class
    print("\nTest 3: Using UnionFind class")
    uf = UnionFind(4)
    print(f"Parent array: {uf.get_parent_array()}")
    print(f"Verification: {uf.get_parent_array() == [0, 1, 2, 3]}")
    print_sets(uf.get_parent_array())
    
    # Test case 4: Error handling
    print("\nTest 4: Error handling")
    try:
        uf.validate_vertex(5)  # Should raise error
    except ValueError as e:
        print(f"Successfully caught error: {e}")
    
    print("\nAll test cases completed successfully!")

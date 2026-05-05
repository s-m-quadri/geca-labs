# Task 6.4: Find and Union Functions
# -----------------------------------
# Extend union-find with:
# 1. find(x) -> returns root parent of x.
# 2. union(x, y) -> merges sets containing x and y.

class UnionFind:
    """
    Union-Find data structure with path compression
    """
    def __init__(self, size):
        """Initialize with size vertices"""
        self.parent = list(range(size))
        self.rank = [0] * size  # For union by rank
        self.size = size
    
    def find(self, x):
        """
        Find the root parent of x with path compression.
        
        Args:
            x: vertex to find root for
            
        Returns:
            Root parent of x
        """
        if x != self.parent[x]:
            # Path compression: Make root the direct parent
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """
        Merge sets containing x and y using union by rank.
        
        Args:
            x, y: vertices whose sets should be merged
            
        Returns:
            True if union was performed, False if already in same set
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
            
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
            
        return True
    
    def connected(self, x, y):
        """Check if x and y are in the same set"""
        return self.find(x) == self.find(y)
    
    def get_sets(self):
        """Get all current sets as a dictionary"""
        sets = {}
        for i in range(self.size):
            root = self.find(i)
            if root not in sets:
                sets[root] = []
            sets[root].append(i)
        return sets

def print_sets(uf):
    """Helper function to print all current sets"""
    sets = uf.get_sets()
    print("\nCurrent sets:")
    for root, members in sets.items():
        print(f"Set with root {root}: {members}")

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic unions
    print("Test 1: Basic unions")
    uf1 = UnionFind(4)
    print_sets(uf1)
    
    uf1.union(0, 1)
    print("\nAfter union(0,1):")
    print(f"find(1) = {uf1.find(1)}")
    print_sets(uf1)
    
    uf1.union(1, 2)
    print("\nAfter union(1,2):")
    print(f"find(2) = {uf1.find(2)}")
    print_sets(uf1)
    
    # Test case 2: Path compression
    print("\nTest 2: Path compression")
    uf2 = UnionFind(5)
    uf2.union(0, 1)
    uf2.union(1, 2)
    uf2.union(2, 3)
    print("Before find operation:")
    print(f"Parent array: {uf2.parent}")
    
    _ = uf2.find(3)  # This should compress the path
    print("After find operation (path compression):")
    print(f"Parent array: {uf2.parent}")
    print_sets(uf2)
    
    # Test case 3: Connected components
    print("\nTest 3: Connected components")
    uf3 = UnionFind(6)
    uf3.union(0, 1)
    uf3.union(2, 3)
    uf3.union(4, 5)
    print_sets(uf3)
    
    print(f"0 and 1 connected: {uf3.connected(0, 1)}")  # True
    print(f"1 and 2 connected: {uf3.connected(1, 2)}")  # False
    
    print("\nAll test cases completed successfully!")

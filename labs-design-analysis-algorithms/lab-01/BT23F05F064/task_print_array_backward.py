# -------------------------------------------
# TASK: Print Elements of Array in Reverse
# -------------------------------------------
# Write two functions:
#   1. print_reverse_recursive(arr): prints last to first using recursion
#   2. print_reverse_iterative(arr): prints using a loop
#
# Example:
#   Input: [1, 2, 3, 4]
#   Output: 4 3 2 1
#
# -------------------------------------------
# HINTS:
# - For recursion, start from last index: len(arr) - 1
# - Reduce index by 1 each call
# - For iteration, use a loop from end to start

def print_reverse_recursive(arr, n):
    if n<0:
        return
    print(arr[n])
    print_reverse_recursive(arr, n-1)
    
def print_reverse_iterative(arr):
    n = len(arr)-1
    while n>=0:
        print(arr[n])
        n-=1

arr = [1,2,3,4]
print("Reverse Recursive:")
print_reverse_recursive(arr, len(arr)-1)

print("\nReverse Iterative:")
print_reverse_iterative(arr)


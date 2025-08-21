# -------------------------------------------
# Problem: Print numbers from n to 1
# -------------------------------------------
# Goal: Practice recursion vs iteration
# -------------------------------------------

def countdown_recursive(n):
    if n <= 0:
        return
    print(n)
    countdown_recursive(n - 1)

def countdown_iterative(n):
    for i in range(n, 0, -1):
        print(i)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("Recursive:")
    countdown_recursive(n)
    print("\nIterative:")
    countdown_iterative(n)

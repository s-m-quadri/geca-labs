# -------------------------------------------
# TASK: Reverse the Digits of a Number
# -------------------------------------------
# Write two functions:
#   1. reverse_digits_recursive(n): recursive
#   2. reverse_digits_iterative(n): loop-based
#
# Example:
#   Input: 1234
#   Output: 4321
#
# -------------------------------------------
# HINTS:
# - Recursive version can peel off last digit using n % 10
# - You may pass an extra parameter (e.g., accumulator) if needed
# - Iterative version: use while-loop and integer math


def reverse_digits_recursive(n, acc=0):     

    # Base case: if n is 0, return the accumulated result
    if n == 0:
        return acc
    else:
        # Peel off the last digit and add it to the accumulator
        last_digit = n % 10
        acc = acc * 10 + last_digit
        # Recur with the remaining digits
        return reverse_digits_recursive(n // 10, acc)   

def reverse_digits_iterative(n):            

    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10
    return reversed_num         
  

# Example usage:        
if __name__ == "__main__":
    num = 1234
    print("Recursive:", reverse_digits_recursive(num))  # Output: 4321
    print("Iterative:", reverse_digits_iterative(num))  # Output: 4321
    # If n is 0, return the accumulated result
    # Peel off the last digit and add it to the accumulator
    # Recur with the remaining digits   
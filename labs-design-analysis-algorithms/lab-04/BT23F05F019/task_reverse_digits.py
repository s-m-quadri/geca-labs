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

<<<<<<<< HEAD:labs-design-analysis-algorithms/lab-01/BT23F05F064/task_reverse_digits.py
def reverse_digits_recursive(num,sum=0):
    if num<=0:
        return sum

    rem = num%10
    sum= sum*10+rem
    return reverse_digits_recursive(num//10,sum)

num = 1234
print(reverse_digits_recursive(num))
========
def reverse_digits_recursive(n, acc=0):
	if n == 0:
		return acc
	return reverse_digits_recursive(n // 10, acc * 10 + (n % 10))

def reverse_digits_iterative(n):
	rev = 0
	while n > 0:
		rev = rev * 10 + (n % 10)
		n //= 10
	return rev

# Example run
print(reverse_digits_recursive(1234))
print(reverse_digits_iterative(1234))
>>>>>>>> sub-lab-daa-04:labs-design-analysis-algorithms/lab-04/BT23F05F019/task_reverse_digits.py

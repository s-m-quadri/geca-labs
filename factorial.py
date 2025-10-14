def recursive(n):
    if n==0:
      return 1
    return  n* recursive(n-1)


def iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 
n=5
print('recursive:',recursive(n))
print('iterative:',iterative(n))
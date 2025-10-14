def factorial_iterative(n):
    result = 1
    for i in range(2 ,n + 1):
       result *= i
    return result  
n = 5 
print("Iterative: " , factorial_iterative(n))

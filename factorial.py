def fact(n):
    if(n==0):
      return 1
    return n*fact(n-1)


def factorial(n):
    if n==0:
     return 0
    result=1
    for i in range(2,n+1):
      result*=i
    return result

      
   
s=input("enter a number ")
a=int(s)
print(fact(a))
print(factorial(a))

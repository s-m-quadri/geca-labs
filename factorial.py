def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

ans=fact(5) 
def fact2(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
ans1=fact2(4)
print(ans1)         
print(ans)   
        
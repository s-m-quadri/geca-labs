# Create a menu:
#  1. Greet user
#  2. Print current time
#  3. Exit

# 💡 TIP:
# Use `while True` with `if` and `break`.
import time
while(True):
    print("menu: \n1.Greet user \n2.print current time  \n3.Exit")
    n=int(input("enter your choice:"))
    if n==1:
        print("Hello user!")
    elif n==2:
        print(time.ctime())   
    elif n==3:
        break     
    else:
        print("Invalid choice")    
    print("***************************")        
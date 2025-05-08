def sum(n):
    if(n==1):
        return 1
    else:
        return n*sum(n-1)
n = eval(input("Enter number to find Sum:"))
sum = sum(n)
print("Sum of first",n,"numbers is" ,sum)
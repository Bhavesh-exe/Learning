n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
for i in range(1,n1+1):
    if(n1%i==0 and n2%i==0):
        gcd=i
print(gcd)
lower=eval(input("Enter the lower range: "))
upper=eval(input("Enter the upper range: "))
for n in range(lower,upper + 1):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            print(n)
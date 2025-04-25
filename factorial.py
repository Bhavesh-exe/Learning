def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a - 1)
    
number = int(input("Enter the no. to calculate factorial: "))
factorial = fact(number)
print(f"Factorial of {number} is {factorial}")

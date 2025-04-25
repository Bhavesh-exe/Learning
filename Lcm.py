# write a program to compute LCM taking input from the user

def lcm(a,b):
    greater = max(a,b)
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater+=1

    return lcm

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))

print(f"LCM of {num1} and {num2} is {lcm(num1,num2)}")
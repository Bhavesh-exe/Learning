def perfect_square(n):
    for i in range(1,n+1):
        if i*i == n:
            return True
    return False

n = int(input("Enter a number: "))
if perfect_square(n):
    print("Yes, it is a perfect square.")
else:
    print("No, it is not a perfect square.")
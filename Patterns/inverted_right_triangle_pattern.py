n = int(input('Enter no of rows: '))
for i in range(n+1):
    x="* "
    x=x* (n-i)     # Replace i with n-i for inverted
    print(f"{x:^1}")

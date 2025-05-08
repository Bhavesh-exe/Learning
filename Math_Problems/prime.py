#check whether the no is prime or not
n = int(input('Enter a number: '))

for i in range(2,n):
    if n % i == 0:
        print(f'The number {n} is Not Prime')
        break
else:
    print(f'The number {n} isPrime')
# This program finds the largest prime factor of n.


n = int(input("Enter a number: "))

largest = 1
i = 2

while i <= n:
    if (n % i == 0):
        largest = i
        n = n // i
    else:
        i = i + 1

print("Largest prime factor is:", largest)
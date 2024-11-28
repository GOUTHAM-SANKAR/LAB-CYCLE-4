num = int(input("Enter a number: "))

X = 0
while num > 0:
    digit = num % 10
    X = X * 10 + digit
    num //= 10

print("Reversed number:",X)
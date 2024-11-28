L = int(input("Enter the lower limit: "))
U = int(input("Enter the upper limit: "))

print("Armstrong numbers between", L, "and", U, "are:")
for num in range(L, U + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit **order
        temp //= 10

    if num == sum:
        print(num)

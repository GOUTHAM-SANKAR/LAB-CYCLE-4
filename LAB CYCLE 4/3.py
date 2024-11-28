N=int(input("Enter a number"))

if N<=1:
    print(N,"is not a prime number")
else:
    for i in range(2,N):
        if (N % i) == 0:
            print(N,"is not a prime number")
            break
    else:
        print(N,"is a prime number")
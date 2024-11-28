A=input("Enter a Single character")

if len(A)==1:
    print("You entered:", A)
    if A.isalpha():

        if A.lower() in "aeiou" :
            print(A, "is a vowel")
        else:
            print(A, "is a consonant")
    elif A.isdigit():
        print(A, "is a digit")
    else:
        print(A, "is a special character")
else:
    print("You entered more than one character.")
num = int(input("Enter a number: "))

if num <= 1:
    print("This is not a prime number")
else:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print("This is not a prime number")
            break
    else:
        print("This is a prime number")
 
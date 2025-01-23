def prime_checker(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)


# A prime number is a number which is divisible by 1 or itself
# 1 / 1
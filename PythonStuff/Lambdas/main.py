def is_this_prime(num: int) -> bool:
    if num.isdigit():
        is_prime = True
        for i in range(2, int(num)):
            if int(num) % i == 0:
                is_prime = False
        return is_prime
    else:
        print("Invalid input. Please type a digit")


num = "Hello"
if num:
    print("this")

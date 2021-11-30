# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
def divisors(number: int) -> list:
    divisors_list = []
    for i in range(1, number+1):
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list

# print(divisors(12))

# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function


def is_factor(num1: int, num2: int) -> bool:
    if num1 in divisors(num2) or num2 in divisors(num1):
        return True
    else:
        return False

# print(is_factor(4, 6))


# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet


def alphabet_position(letter: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    return alphabet.index(letter.lower())

# print(alphabet_position("C"))

# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14


def id_generator(name_string: str) -> str:
    id = ""
    for letter in name_string:
        position = alphabet_position(letter)
        id += str(position)
    return id


# print(id_generator("Bob"))

# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

def password_generator(name_string: str) -> str:
    number = 0
    for i in id_generator(name_string):
        number += int(i)
    return str(int(id_generator(name_string)) - number)

print(password_generator("Bob"))












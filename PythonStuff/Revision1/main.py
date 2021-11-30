# function which takes a string input of a big number
# loop through the number and create two totals, even position totals and odd position totals
# even totals * 3 + odd totals
# if 0 then return 0 else return 10 minus last digit


def function1(number: str):
    even_count = 0
    odd_count = 0
    counter = 0
    for digit in number:
        if counter % 2 == 0:
            even_count += int(digit)
        else:
            odd_count += int(digit)
        counter += 1
    result = even_count*3 + odd_count
    last_digit = str(result)[-1]
    if last_digit == "0":
        return 0
    else:
        return 10 - int(last_digit)



print(function1("1212"))
print("we are no longer in the function")


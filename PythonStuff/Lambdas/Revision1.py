def computr_check(num1: str) -> int:

even_num = 0

odd_num = 0

result = 0


def func(num1):
        even_num = 0
        odd_num = 0
        result = 0
        for w in num1:
            position = num1.index(w)
            if position % 2== 0:
                even_num += position
            else:
                odd_num += position
                result = even_num *3
                result += odd_num
            if result[-1] == 0:
                return result - 10
            return result


print(func("914468"))
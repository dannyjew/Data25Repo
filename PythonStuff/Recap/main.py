input1 = "Hello"
input2 = "Helol"


for i in input1:
    print(i)

print("Now for the while loop")

i = 0
while True:
    if input1[i] == 'l':
        break
    else: print(input1[i])
    i += 1

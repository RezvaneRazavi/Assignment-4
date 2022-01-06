import random
array = []

lenght_array = int(input('enter lenght array: '))

for i in range(lenght_array):
    x = int(input('enter number: '))

    if x not in array:
        array.append(x)

array.sort()

print(array)
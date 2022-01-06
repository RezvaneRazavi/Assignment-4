num = int(input('enter a number: '))
n = num

while n > 1:
    for i in range(2, num+1):
        if n % i == 0:
            n /= i

        else:
            break
    break

if n == 1:
    print('yes,', num, 'is a factorial number')
else:
    print('no,', num, 'is not a factorial number')


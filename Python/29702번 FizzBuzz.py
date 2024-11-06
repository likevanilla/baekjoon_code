l = []
num = 0
for _ in range(3):
    l.append(input())
    
for i in range(3):
    if l[i] != 'Fizz' and l[i] != 'Buzz' and l[i] != 'FizzBuzz':
        l[i] = int(l[i])
        if l.index(l[i]) == 0:
            num = l[i] + 3
        elif l.index(l[i]) == 1:
            num = l[i] + 2
        elif l.index(l[i]) == 2:
            num = l[i] + 1

if num % 3 == 0 and num % 5 == 0:
    print('FizzBuzz')
elif num % 3 == 0 and num % 5 != 0:
    print('Fizz')
elif num % 3 != 0 and num % 5 == 0:
    print('Buzz')
else:
    print(num)
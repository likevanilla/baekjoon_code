n = 0
a = 0
for _ in range(10):
    n = int(input())
    if n == 1:
        a += 90
    elif n == 2:
        a += 180
    elif n == 3:
        a -= 90

if abs(a) % 360 == 0:
    print('N')
elif abs(a) % 360 == 90:
    print('E')
elif abs(a) % 360 == 180:
    print('S')
elif abs(a) % 360 == 270:
    print('W')

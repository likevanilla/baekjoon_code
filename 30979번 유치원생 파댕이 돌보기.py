t = int(input())
n = int(input())
f = list(map(int, input().split()))

for i in f:
    t -= i

if t > 0:
    print('Padaeng_i Cry')
else:
    print('Padaeng_i Happy')
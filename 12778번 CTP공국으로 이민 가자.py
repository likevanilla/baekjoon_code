t = int(input())
result = []
count = []

for _ in range(t):
    m, type = input().split()
    m = int(m)
    count.append(m)
    p = list(input().split())
    if type == 'C':
        for i in range(m):
            result.append(ord(p[i])-64)
    elif type == 'N':
        for j in range(m):
            result.append(chr(int(p[j])+64))

A = 0
for k in range(t):
    for x in range(count[k]):
        print(result[A+x], end=' ')
    A += x+1
    print()
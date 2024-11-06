n, k = map(int,input().split())
p = list(range(1,n+1))
d = []

a = 0
while p:
    a = (a + k -1) % len(p)
    d.append(p.pop(a))

print('<', end='')
for i in range(n-1):
    print(d[i], end=', ')
print(d[n-1], end = '')
print('>', end='')
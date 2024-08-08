n, k = map(int, input().split())
npac = 1
kpac = 1
nkpac = 1

for i in range(1, n+1):
    npac *= i

for j in range(1, k+1):
    kpac *= j

for x in range(1,n-k+1):
    nkpac *= x

print(int(npac/(nkpac*kpac)))
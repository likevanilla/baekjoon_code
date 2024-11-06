K = int(input())
Nlist = []
sum = 0

for i in range(K):
    N = int(input())
    if N != 0:
        Nlist.append(N)
    else:
        Nlist.pop()

for j in Nlist:
    sum += j

print(sum)
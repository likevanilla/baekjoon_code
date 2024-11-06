M = int(input())
N = int(input())
result = []
count = 0

for i in range(M,N+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        result.append(i)

if 1 in result:
    result.remove(1)

if len(result) == 0:
    print('-1')
else:
    for x in result:
        count += x
    print(count)
    print(min(result))
l = []
t = int(input())
result = []

for _ in range(t):
    k = int(input())
    n = int(input())
    cnt = 0
    home = list(range(1,n+1))
    for i in range(k):
        for j in range(1,n+1):
            home.append(sum(home[cnt:j+cnt]))
        cnt += n
    result.append(home.pop())

for x in result:
    print(x)
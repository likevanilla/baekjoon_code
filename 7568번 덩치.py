n = int(input())
rank = []
data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a,b))

for i in range(n):
    count = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    rank.append(count + 1)

for x in rank:
    print(x, end=' ')
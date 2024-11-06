import math

t = int(input())
result = []

for _ in range(t):
    a, b = map(int, input().split())
    result.append(math.lcm(a, b))

for i in result:
    print(i)
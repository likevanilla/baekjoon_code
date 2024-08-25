import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    l.append([a, b])
l.sort(key = lambda x: (x[1], x[0]))

for x in l:
    print(x[0], x[1])
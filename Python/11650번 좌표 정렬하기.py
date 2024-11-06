import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    [a, b] = map(int, sys.stdin.readline().split())
    l.append([a, b])
l.sort()
for x in l:
    print(x[0], x[1])
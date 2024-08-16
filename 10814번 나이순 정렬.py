import sys

n = int(sys.stdin.readline())
l = []
for _ in range(n):
    a, b = sys.stdin.readline().split()
    a = int(a)
    l.append((a,b))
    
l.sort(key = lambda x: x[0])

for x in l:
    print(x[0], x[1])
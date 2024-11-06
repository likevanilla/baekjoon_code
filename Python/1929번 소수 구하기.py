import sys

M, N = map(int, sys.stdin.readline().split())
arr = [False, False] + [True] * (N - 1)

p = 2
while p * p <= N:
    if arr[p]:
        for i in range(p * p, N + 1, p):
            arr[i] = False
            
    p += 1
    
for x in range(M, N + 1):
    if arr[x]:
        print(x)
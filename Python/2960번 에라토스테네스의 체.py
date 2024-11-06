import sys
N, K = map(int, sys.stdin.readline().split())
count = 1
arr = [True] * (N + 1)

for i in range(2, N + 1):
    if arr[i]:
        for j in range(i, N + 1, i):
            if arr[j] == False:
                continue
            
            if count == K:
                print(j)
            
            arr[j] = False
            count += 1
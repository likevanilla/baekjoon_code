import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    index = [i for i in range(n)]
    
    count = 0
    while True:
        if queue[0] == max(queue):
            count += 1
            if index[0] == m:
                print(count)
                break
            else:
                queue.pop(0)
                index.pop(0)
        else:
            queue.append(queue.pop(0))
            index.append(index.pop(0))

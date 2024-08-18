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
        if queue[0] == m:
            print(count)
            break
        else:
            del queue[0]
            del index[0]
    else:
        queue.append(queue[0])
        del queue[0]
        index.append(index[0])
        del index[0]
    
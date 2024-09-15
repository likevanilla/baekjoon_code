from collections import deque

n, m = map(int, input().split())
queue = deque(range(1, n+1))
num = deque(map(int, input().split()))
count = 0

while len(num) != 0:
    if queue[0] == num[0]:
        queue.popleft()
        num.popleft()
        
    elif queue.index(num[0]) >= len(queue)/2:
        queue.rotate(1)
        count += 1
        
    elif queue.index(num[0]) < len(queue)/2:
        queue.rotate(-1)
        count += 1

print(count)
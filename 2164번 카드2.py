import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque(range(1,n+1))

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()

print(card[0])
N = int(input())
result = []
card = list(range(1,N+1))

for _ in range(N):
    if card:
        result.append(card[0])
        card.pop(0)
        if card:
            card.append(card[0])
            card.pop(0)

print(*result)
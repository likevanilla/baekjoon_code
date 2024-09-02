n, m = map(int, input().split())
board = []
count = []

for _ in range(n):
    board.append(input())
    
for x in range(n-7):
    for y in range(m-7):
        w = 0
        b = 0   
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'B':
                        w += 1
                    if board[i][j] != 'W':
                        b += 1
                else:
                    if board[i][j] != 'W':
                        w += 1
                    if board[i][j] != 'B':
                        b += 1
        count.append(min(w, b))

print(min(count))
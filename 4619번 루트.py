import sys

while True:
    b, n = map(int, sys.stdin.readline().split())
    if b == n == 0:
        break
    
    a = 0
    while a ** n < b:
        a += 1
    
    if a ** n - b < b - (a - 1) ** n:
        print(a)
    else:
        print(a - 1)
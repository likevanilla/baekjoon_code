import sys

N = int(sys.stdin.readline())
num = []

for _ in range(N):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    print(i)
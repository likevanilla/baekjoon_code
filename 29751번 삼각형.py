import sys

w, h = map(int, sys.stdin.readline().split())
result = w * h / 2

print('{:.1f}'.format(result))
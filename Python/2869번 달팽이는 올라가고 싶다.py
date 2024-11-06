import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
count = 0

count = ((v - a) / (a - b)) + 1

print(math.ceil(count))
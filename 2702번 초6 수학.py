import math
import sys

t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(math.lcm(a,b), math.gcd(a,b))
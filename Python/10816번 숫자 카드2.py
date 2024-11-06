import sys
 
n = sys.stdin.readline()
card = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline()
find = list(map(int, sys.stdin.readline().split()))

count = {}

for x in card:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1

for i in find:
    if i in count:
        print(count[i], end = ' ')
    else:
        print('0', end = ' ')
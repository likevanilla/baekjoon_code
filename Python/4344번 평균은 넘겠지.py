import sys

c = int(sys.stdin.readline())
for _ in range(c):
    l = list(map(int, sys.stdin.readline().split()))
    avg = (sum(l)-l[0])/l[0]
    count = 0
    del l[0]
    for x in l:
        if x > avg:
            count += 1
            
    print("{0:.3f}%".format((count/len(l)) * 100))
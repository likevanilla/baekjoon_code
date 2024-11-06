import sys

n = int(sys.stdin.readline())
a = 1

if n == 0:
    print('0')
    sys.exit()
else:
  for i in range(2, n+1):
    a = a * i

num = list(map(int, str(a)))
if num[-1] == 0:
    count = 0
    for x in range(len(num)):
        if num[-1-x] == 0:
            count += 1
        else:
            break
    
else:
    count = 0

print(count)
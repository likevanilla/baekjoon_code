import sys

n = int(sys.stdin.readline())
l = []
stack = []
result = []
count = 1

for _ in range(n):
    l.append(int(sys.stdin.readline()))
    
for x in l:
    while count <= x:
        stack.append(count)
        result.append('+')
        count += 1
    
    if stack[-1] == x:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        sys.exit()

for i in result:
    print(i)
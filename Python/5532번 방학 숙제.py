l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
count = []

if a % c == 0:
    count.append(int(a/c))
else:
    count.append(int(a/c+1))
    
if b % d == 0:
    count.append(int(b/d))
else:
    count.append(int(b/d+1))

print(l-max(count))
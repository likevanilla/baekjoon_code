import sys

n, k = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(int(sys.stdin.readline()))
    
cm = 1
longest = max(l)

while cm <= longest:
    mid = (cm + longest) // 2
    lan = 0
    
    for i in l:
        lan += i // mid
    
    if lan >= k:
        cm = mid + 1
    else:
        longest = mid - 1
        
print(longest)
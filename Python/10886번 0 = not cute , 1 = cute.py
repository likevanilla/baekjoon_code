n = int(input())
ans = []

for _ in range(n):
    ans.append(int(input()))

if ans.count(0) > ans.count(1):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
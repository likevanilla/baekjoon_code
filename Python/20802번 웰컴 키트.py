n = int(input())
shirt = list(map(int, input().split()))
t, p = map(int, input().split())
t_count = 0
p_count = 0

for x in shirt:
    if x == 0:
        t_count += 0
    elif x % t == 0:
        t_count += int(x / t)
    else:
        t_count += int(x / t + 1)

p_count = int(n / p)

print(t_count)
print(p_count, n-p_count*p)
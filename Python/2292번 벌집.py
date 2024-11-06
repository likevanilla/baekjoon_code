n = int(input())
bee = 1
count = 1

while n > bee:
    bee += 6 * count
    count += 1

print(count)
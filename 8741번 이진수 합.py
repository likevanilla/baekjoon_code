k = int(input())
n = 2**k-1
m = n * (n+1) // 2

print(bin(m)[2:])
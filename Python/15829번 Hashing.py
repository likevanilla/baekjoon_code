M = 1234567891
r = 31
L = int(input())
alp = input()
result = 0

for i in range(len(alp)):
    num = ord(alp[i]) - 96
    result += num * (r ** i)

print(result % M)
s = input()
lst = [0] * 26

for i in s:
    lst[ord(i)-97] += 1

for j in lst:
    print(j, end=' ')
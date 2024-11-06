import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

answer1 = round(sum(num) / n)
print(answer1) 

answer2 = num[n//2]
print(answer2)

dic = dict()
for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mx = max(dic.values())
mx_dic = []

for j in dic:
    if mx == dic[j]:
        mx_dic.append(j)

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

answer4 = abs(num[0] - num[-1]) 
print(answer4)
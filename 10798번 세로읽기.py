import sys

sen = []
result = []
length = []
for _ in range(5):
    sen.append(sys.stdin.readline().rstrip())
    length.append(len(sen[-1]))

for i in range(max(length)):
    for j in range(5):
        if len(sen[j]) > i:
            result.append(sen[j][i])
        
for x in result:
    print(x, end='')
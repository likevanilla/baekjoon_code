#두번째 시도의 코드
import sys

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

n = int(sys.stdin.readline())
 
if n:
    dif = []
    avg = round(n * 0.15)
    
    for _ in range(n):
        dif.append(int(sys.stdin.readline()))
    dif.sort()
    dif = dif[avg:n-avg]
      
    result = round(sum(dif) / len(dif))
    print(result)
else:
    print(0)
    
#첫 시도와 유사한 코드
import sys

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

n = int(sys.stdin.readline())

if n:
    dif = []
    avg = round(n * 0.15)
    
    for _ in range(n):
        dif.append(int(sys.stdin.readline()))
    
    dif.sort()
    
    if avg > 0:
        del dif[:avg]
        del dif[-avg:]
    
    result = round(sum(dif) / len(dif))
    print(result)
else:
    print(0)

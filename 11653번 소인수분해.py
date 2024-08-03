N = int(input())
index = 2
arr = []

while N:
    if N % index == 0:
        N = int(N / index)
        arr.append(index)
    else:
        index += 1
    
    if N == 1:
        break        

for x in arr:
    print(x)
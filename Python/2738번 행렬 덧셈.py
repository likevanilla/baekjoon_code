M, N = map(int, input().split())
num_list1 = []
num_list2 = []
result = []
count = 0

for _ in range(M):
    list1 = list(map(int, input().split()))
    for i in range(N):
        num_list1.append(list1[i])

for _ in range(M):
    list2 = list(map(int, input().split()))
    for j in range(N):
        num_list2.append(list2[j])

for x in range(M*N):
    result.append(num_list1[x] + num_list2[x])

for a in range(M):
    for y in range(N):
        print(result[count+y], end=' ')
    count += N
    print()
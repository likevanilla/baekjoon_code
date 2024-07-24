N = int(input())

for j in range(N):
    stack = []
    PS_list = input()
    
    for i in PS_list:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:            
        if stack:
            print('NO')
        else:
            print('YES')
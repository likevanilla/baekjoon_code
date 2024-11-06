import sys

n = int(sys.stdin.readline())
queue = []


for _ in range(n):
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'push':
        queue.append(int(command[1]))
    
    if command[0] == 'pop':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
            queue.remove(queue[0])
    
    if command[0] == 'size':
        print(len(queue))
    
    if command[0] == 'empty':
        if len(queue) != 0:
            print('0')
        else:
            print('1')
            
    if command[0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    
    if command[0] == 'back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
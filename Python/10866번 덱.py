from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

while n > 0:
    n -= 1
    command = list(sys.stdin.readline().split())
    
    if command[0] == 'push_front':
        queue.appendleft(command[1])
        
    elif command[0] == 'push_back':
        queue.append(command[1])
        
    elif command[0] == 'pop_front':
        if not queue:
            print('-1')
        else:
            print(queue.popleft())
            
    elif command[0] == 'pop_back':
        if not queue:
            print('-1')
        else:
            print(queue.pop())
                        
    elif command[0] == 'size':
        print(len(queue))
    
    elif command[0] == 'empty':
        if queue:
            print('0')
        else:
            print('1')
    
    elif command[0] == 'front':
        if not queue:
            print('-1')
        else:
            print(queue[0])
    
    elif command[0] == 'back':
        if not queue:
            print('-1')
        else:
            print(queue[-1])
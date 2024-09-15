num = input()
numlist = list(num)
sum = 0

for i in range(len(num)):
    rotated = int("".join(numlist))
    sum += rotated
    
    numlist.append(numlist.pop(0))
    
print(sum)
b = []
s = []
for _ in range(3):
    b.append(int(input()))

for x in range(2):
    s.append(int(input()))
    
print(min(b)+min(s)-50)
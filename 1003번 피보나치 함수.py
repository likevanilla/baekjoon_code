import sys

dp = [-1] * 41
count0 = [0] * 41
count1 = [0] * 41

dp[0] = 0
dp[1] = 1
count0[0] = 1
count1[1] = 1

def fibonacci(n):
    if dp[n] != -1:
        return
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        count0[i] = count0[i-1] + count0[i-2]
        count1[i] = count1[i-1] + count1[i-2]
    
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    fibonacci(n)
    print(count0[n], count1[n])
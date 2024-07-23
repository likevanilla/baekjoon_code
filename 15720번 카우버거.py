B, C, D = map(int, input().split())
price_before = 0


B_price = list(map(int, input().split()))
C_price = list(map(int, input().split()))
D_price = list(map(int, input().split()))

B_price = sorted(B_price, reverse=True)
C_price = sorted(C_price, reverse=True)
D_price = sorted(D_price, reverse=True)

for i in range(B):
    price_before += B_price[i]
for j in range(C):
    price_before += C_price[j]
for k in range(D):
    price_before += D_price[k]
    
print(price_before)

A = [B, C, D]
price_after = 0
E = 0

for n in range(min(A)):
    price_after = price_after + ((B_price[n] + C_price[n] + D_price[n]) * 0.9)
    E += B_price[n] + C_price[n] + D_price[n]
    
print(int(price_after + (price_before - E)))
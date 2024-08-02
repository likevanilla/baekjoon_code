N = int(input())
P = int(input())

if N <= 4:
    print(P)
elif 5 <= N <= 9:
    if P - 500 > 0:
        print(P-500)
    else:
        print(0)
elif 10 <= N <= 14:
    if P*0.9 < P-500:
        print(int(P*0.9))
    else:
        if P-500 < 0:
            print(0)
        else:
            print(P-500)
elif 15 <= N <= 19:
    if P - 2000 < P * 0.9:
        if P - 2000 > 0:
            print(P-2000)
        else:
            print(0)
    else:
        print(int(P*0.9))
elif N >= 20 :
    if P * 0.75 < P - 2000:
        print(int(P*0.75))
    else:
        if P - 2000 > 0:
            print(P-2000)
        else:
            print(0)
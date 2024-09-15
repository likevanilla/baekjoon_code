while True:
    sentence = list(map(str, input().split()))
    if sentence[0] == '*':
        break
    
    judge = set()
    
    for i in sentence:
        letter = i[0].upper()
        judge.add(letter)

    if len(judge) == 1:
        print('Y')
    else:
        print('N')
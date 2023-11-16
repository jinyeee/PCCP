# while문 사용

# while True:

value = list(map(int, input().split()))
while int(input()) == 0:
    value = input()
    test = []
    test2 = []
    for i in value:
        test.append(i)
        for j in value[::-1]:
            test2.append(j)
        if test == test2:
            print('yes')
        else:
            print('no')    





# 입력받기

# n, m을 입력받아서 무언가를 
# split 구분자를 기준으로 문자열을 구분하여 잘라준다.


a = input()
print(a)


#반복할 횟수를 입력받는다
# 입력받은 횟수만큼 반복 T : 5

# 입력받은 두 수를 나눠준다. ex) 1 7  -> a:1 , b:7
#T = input()
T = int(input()) # 형변환이 필요
for _ in range(T):
    x = input().split()
    new_list = []
    for i in x:
        new_list.append(int(i))
    print(x)

    #.split() => ['1', '6']
    # 메서드 -> 리턴값이 존재
    # 리턴값을 원하는 변수에 넣어줄수있다.
    # 새로운 리스트를 생성하고 원하는 형변환을 해주면서
    # 리스트에 값을 추가.


    #map(func, container)
    x = list(map(int, x))
    print(x)


T = int(input()) # 형변환이 필요
for _ in range(T):
    x = input().split()
    x = list(map(int, x))
    print(x)


T = int(input()) # 형변환이 필요
for _ in range(T):
    input_value = input()
    input_value = input().split()
    input_value = list(map(int, input_value))
    #input_value = list(map(int, input().split()))
    print(input_value)

    # new_list = []
    # for i in x:
    #     new_list.append(int(i))
    # print(x)    
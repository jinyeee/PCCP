# n, m을 입력받아서, 무언가를 해라.
# a = input()
# print(a)
#
# a = input()
# print(a)
#
# a = input()
# print(a)
#
# a = input()
# print(a)
#
# a = input()
# print(a)
#
# a = input()
# print(a)

# T = input()
T = int(input())
print(T)
for _ in range(T):
    input_value = input() # str 으로써 입력을 받는다.
    print(input_value)

    input_value = input_value.split() # 리스트의 형태로 바꿔준다.
    print(input_value)

    input_value = list(map(int, input_value)) # 리스트의 원소들을 각각 정수로 바꿔준다
    print(input_value)

    # input_value = list(map(int,input().split()))
    a, b = input_value
    print(a, b)
    # new_lst = []
    # for i in x:
    #     new_lst.append(int(i))
    # new_lst = [ int(char) for char in x]


# 5
# 1 6
# 3 7
# 6 2
# 7 100
# 9 635
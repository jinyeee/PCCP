# lst = [1, 3, 2, 6, 8, 7, 4]
lst = [8, 5, 1, 4, 3, 6, 0]

# 0번째, 1번째의 값을 swap 하는 방법
# lst[0], lst[1] = lst[1], lst[0]
# print(lst)

# swap을 통해 가장 큰 값을 가장 오른쪽에 두자.
# 힌트 : "상태", i와 i+1을 비교

for max_index in range(len(lst) - 1, 0, -1):
    # for i in range(len(lst)-1):
    for i in range(max_index):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)
#
# for num in range(len(lst)-1, 0, -1):
#     num = len(lst)-1
#     num = len(lst)-2
#     num = len(lst)-3
#     len(lst) - 1

for max_index in range(len(lst) - 1, 0, -1):
    # for i in range(len(lst)-1):
    for i in range(max_index):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)



# for num in range(len(lst)):
#     num = 0
#     len(lst) - 1 - num
#     len(lst) - 1
#
#     num = 1
#     len(lst) - 1 - num
#     len(lst) - 2
#
#     num = 2
#     len(lst) - 1 - num
#     len(lst) - 3
#
for index in range(1, len(lst)):
    # for i in range(len(lst)-1):
    max_index = len(lst) - index
    for i in range(max_index):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)







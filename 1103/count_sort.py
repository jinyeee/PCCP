# counting sort
# 정수밖에 정렬을 하지 못합니다.
# 대신, 엄청 빠릅니다. O(n+k), n은 개수, k는 가장 큰 정수
# 불안정해요.
# 단, 안정화 시킬수는 있습니다.

lst = [1, 3, 3, 2, 2, 1, 3, 4, 1]

counting_lst = [0] * (max(lst) + 1) # 0번째 index는 무시
# 번째 라는 개념과 숫자를 맞추기 위해서.

# 개수를 셉니다.
for num in lst:
    counting_lst[num] += 1

print(counting_lst)

sorted_lst = []
for index in range(len(counting_lst)):
    value = counting_lst[index]
    for _ in range(value):
        sorted_lst.append(index)

print(sorted_lst)

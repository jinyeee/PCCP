# 1.가장 큰 / 작은 수가 들어가야 할 위치의 index를 잡는다.
# 2. 가장 큰 / 작은 수의 인덱스를 찾는다
# 3. 수가 들어갈 위치와 교체한다.
lst = [10, 8, 7, 6, 4, 3,9]

for index in range(len(lst)):
    min_index = index # 가장 작은 숫자가 들어갈 index

    for i in range(index, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    lst[min_index], lst[index] = lst[index], lst[min_index]
    print(lst)

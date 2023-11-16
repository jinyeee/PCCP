lst = [2, 3, 4, 5]

def my_len(lst):
    count = 0
    for _ in lst:
        count = count + 1

    return count

def my_sum(lst):
    total = 0
    for num in lst:
        total = total + num
    return total

def my_max(lst):
    # max_num = float('-inf')
    max_num = lst[0]

    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

def my_min(lst):
    min_num = lst[0]
    for num in lst:
        if num < min_num:
            min_num = num
    return min_num

def my_reversed(lst):
    reversed_lst = []
    for index in range(my_len(lst) - 1, -1, -1):
        num = lst[index]
        reversed_lst.append(num)
        # reversed_lst += [num]
    return reversed_lst
print(my_reversed(lst))

def my_reversed(lst):
    reversed_lst = []
    for index in range(my_len(lst)):
        index += 1
        index *= -1
        num = lst[index]
        reversed_lst += [num]
    return reversed_lst
print(my_reversed(lst))




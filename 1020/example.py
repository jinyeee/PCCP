# 1. 다음 리스트를 만들어보세요 (여러가지 방법으로 만들어보세요)
# 	a. [0, 1, 2, 3, 4, 5]
# 	b. [4, 5, 6, 7]
# 	c. [3, 6, 9]
# 	d. [1, 2, 1, 2, 1, 2, 1, 2]

# [0, 1, 2, 3, 4, 5]
print(list(range(0, 6)))

print(list(range(4, 8)))
print(list(range(8))[4:])

print(list(range(3, 9 + 1, 3)))

lst = []
for num in [1,2,3]:
    lst.append(num * 3)

print(lst)
print(list(range(1, 3))*4)

# snake case - python's pick
# hello_my_name_is_jun

# camel case
# helloMyNameIsJun

# pascal case
# HelloMyNameIsJun
lst = []
for _ in range(4):
    # lst.append(1)
    # lst.append(2)
    lst = lst + [1, 2]
print(lst)

# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, ]
lst = []
for _ in range(3):
    for i in range(1, 5):
        lst.append(i)
    # lst.append(1)
    # lst.append(2)
    # lst.append(3)
    # lst.append(4)
print(lst)



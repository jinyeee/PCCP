# python function scope
a = 1
lst = [1, 2, 3]

def func():
    a = 3
    print(a)
    print(lst)
    lst[0] = 100
    # lst = [100, 1, 2]
    print(lst)

func()
# print(b)
print(a)
print(lst)
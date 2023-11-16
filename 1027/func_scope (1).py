# function scope
a = 2
a = 3
a = 1
lst = [1, 2, 3]
print(a)
print(lst)
print()

def func():
    a = 3
    # lst[0] = 100
    lst = [100, 2, 3]
    print(a)
    print(lst)


func()
print()
print(a)
print(lst)






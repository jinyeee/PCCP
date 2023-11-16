a = 1
b = a
a = 3
print(a, b)

lst1 = [1, 2, 3]
lst2 = lst1
lst1[0] = 100
print(lst1, lst2)
# lst2 라는것은 lst1의 원소의 값만 가져오고 싶다.
# lst2 = []
# for i in lst1:
#     lst2.append(i)


# 얕은 복사. 1차원 리스트 일때만 가능.
lst1 = [1, 2, 3]
lst2 = lst1[:]
lst1[0] = 100
print(lst1, lst2)

# 2차원일때는 불가능합니다.
mat1 = [[1, 2], [3, 4]]
mat2 = mat1[:]
mat1[0][0] = 100
print(mat1)
print(mat2)

from copy import deepcopy
# 얕은 카피를 recursive하게 하면 됩니다.
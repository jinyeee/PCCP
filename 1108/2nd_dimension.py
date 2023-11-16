# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
# gird_1 = [[0] * 4 for _ in range(4)]

# 1.
n = 5
mat = []
num = 1

# 2
# [1, 2, 3, 4]
for _ in range(n):
    lst = []
    for _ in range(n):
        lst.append(num)
        num += 1
    # 3
    mat.append(lst)

# 4 => 반복문으로 처리
# lst = []
# for _ in range(4):
#     lst.append(num)
#     num += 1
#
# mat.append(lst)
from pprint import pprint
pprint(mat)

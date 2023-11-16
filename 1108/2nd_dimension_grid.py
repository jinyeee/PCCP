# mat = []
# for _ in range(4):
#     mat.append([0] * 4)
#
mat = [[0]*4 for _ in range(4)]

num = 1
# for index in range(4):
#     mat[0][index] = num
#     num += 1
#
# for index in range(4):
#     mat[1][index] = num
#     num += 1
#
# for index in range(4):
#     mat[2][index] = num
#     num += 1

for i in range(4):
    for j in range(4):
        mat[i][j] = num
        num += 1
print(mat)







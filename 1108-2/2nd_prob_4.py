
mat = [[0]*4 for _ in range(4)]

num = 1
for i in range(4):
    if i % 2 == 0:
        for j in range(4):
            mat[i][j] = num
            num += 1
    else:
        for j in range(4):
            mat[i][3-j] = num
            num += 1
print(mat)



#
# for i in range(4):
#     for j in range(4):
#         if i % 2 == 0:
#             mat[i][j] = num
#         else:
#             mat[i][3 - j] = num
#         num += 1
#

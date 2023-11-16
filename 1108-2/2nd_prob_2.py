# # 2번
# 1 2 4
# 8 16 32
# 64 128 256
mat = [[0]*4 for _ in range(4)]

num = 1
for i in range(4):
    for j in range(4):
        mat[i][j] = num
        num *= 2
print(mat)







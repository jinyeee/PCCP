# 3번
# 0 2 6
# 12 20 30
# 42 56 72

n = 3
mat = [[0]*n for _ in range(n)]

num = 0
for i in range(n):
    for j in range(n):
        mat[i][j] = num * (num+1)
        num += 1
print(mat)







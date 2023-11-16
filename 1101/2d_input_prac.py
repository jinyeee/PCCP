# 4 3
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12

# n : 행의 개수, m은 열의 개수
n, m = list(map(int, input().split()))
print(n, m)
# 나 자신을 믿은거에요.
# 중간중간 무조건 확인하세요.

# 천천히 진행하는 과정

# mat = []
# for _ in range(n):
#     lst = list(map(int,input().split()))
#     mat.append(lst)

# print(mat)

# 한번에 진행하는 과정
mat = [list(map(int, input().split())) for _ in range(n)]

print(mat)


def func(a, b):
    return a + b








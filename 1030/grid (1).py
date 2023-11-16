from pprint import pprint
# import pprint
# pprint.pprint()
n = 5

# 잘못된 방식
# grid = [[0] * n]*n
# pprint(grid)
# grid[0][0] = 100
# print()
# pprint(grid)

# 잘못된 코드. 위와 같은.
grid = []
small_grid = [0]*n
for _ in range(n):
    grid.append(small_grid)

grid = []
for _ in range(n):
    # small_grid = [0]*n
    # grid.append(small_grid)
    grid.append([0]*n)

pprint(grid)
grid[0][0] = 100
print()
pprint(grid)

# 최종형태
grid = [[0]*n for _ in range(n)]

grid = [[0]*5 for _ in range(6)]
print()
pprint(grid)
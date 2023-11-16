mat = []
for i in range(2, 10):
    dan = []
    for j in range(1, 10):
        dan.append(i * j)
    mat.append(dan)

from pprint import pprint
pprint(mat)
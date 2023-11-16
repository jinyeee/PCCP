# 2.
# 구구단 3단을 출력하시오. 단, for, while을 활용하여 다양하게 만들어보시오.

for i in range(1, 10):
    print(3, i, '->', 3 * i)


for i in range(1, 10):
    print(3 * i, end=' ')
print()

for i in range(3, 3 * 10, 3):
    print(i)

dan_3 =list(range(3, 3*10, 3))
print(dan_3)
# packing, unpacking - asterisk(*)를 활용한 방식.
print(*dan_3)





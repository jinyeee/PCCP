# for, while 둘다 반복

# for
# container에 대해서 반복을 진행한다.
# container - 여러 개의 data가 들어있는 자료 구조.
# 여러 개의 data에서 하나씩 뽑아서 그 data를 특정 변수에 저장한 후
# 반복을 진행한다.

# while
# 특정 조건에 따라서 반복을 진행합니다.
# 즉, 반복이 멈추기 위해서는 조건이 변경이 되어야 한다.
# (무한 루프 조심!)

# 숫자 1, 2, 3, 4, 5를 출력하시오.
for num in range(1, 6):
    print(num)
print()

num = 1
while num <= 5:
    print(num)
    num = num + 1
print()

num = 0
while num < 5:
    num = num + 1
    print(num)

# break
# 반복을 멈추는 작용을 함.
num = 0
while True:
    num = num + 1
    print(num)
    if num == 5:
        break
print()

names = ['j', 'a', 'k']

for name in names:
    print(name)
print()

index = 0
while 1:
    name = names[index]
    print(name)

    index += 1
    if index == len(names):
        break
print()


index = 0
while index < len(names):
    name = names[index]
    print(name)

    index += 1
print()

# 숫자가 2, 4면 출력하고
# 숫자가 1, 3이면 출력하기 싫어요.
for i in range(1, 5):
    if i == 1 or i == 3:
        continue
    print(i)

    # if i == 2 or i == 4:
    #     print(i)











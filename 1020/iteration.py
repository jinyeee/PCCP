# for 변수 in container:
#      변수를 활용한 코드

for num in [1, 2, 3, 4, 5]:
    # num = 5
    print(num)

names = ['j', 'a', 'k']

for name in names:
    # print('n번째 학생 누구 있니?')
    print(f'n번째 학생 {name} 있니?')

for index in range(len(names)):
    name = names[index]
    num = index + 1
    print(f'{ index + 1 }번째 학생 { name } 있니?')
    # print(f'{ num }번째 학생 { name } 있니?')

# for index, name in enumerate(names):
#     print(index, name)


# 1부터 10까지 숫자에 대해서
# 2의 배수를 출력하시오.


for num in [2, 4, 6, 8, 10]:
    print(num)

for num in list(range(2, 11, 2)):
    print(num)

for num in list(range(1, 11)):
    if num % 2 == 0:
        print(num)




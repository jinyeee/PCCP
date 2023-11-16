# 1.
# names = ['jun', 'alex', 'ken'] 일 때,
#
# 0번째 손님 : jun
# 1번째 손님 : alex
# 2번째 손님 : ken
# 을 출력하시오. 단, for, while을 활용하여 2번 작성하시오.

# for
names = ['jun', 'alex', 'ken']
for index in range(len(names)):
    name = names[index]
    # index, name 두가지 변수.
    print(f'{index}번째 손님 : {name}')
    #     .format - 예전 버전.

# for index, name in enumerate(names):
#     print(f'{index}번째 손님 : {name}')



# while
index = 0
while True:

    name = names[index]
    print(f'{index}번째 손님 : {name}')

    index += 1
    if index == len(names):
        break

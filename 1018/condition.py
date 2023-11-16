# if문
# 어떤 조건 하에, 실행 여부를 판단하는 구문
money = 2000

# 만약 돈이 1000원보다 많으면
if money > 1000:
    # 그거를 살꺼야.
    print('그거를 살꺼야')
#
# 만약 돈이 1000보다 적으면
if money < 1000:
    # 그거를 못살꺼야.
    print('그거를 못 살꺼야.')

# if 조건 :
#     여기에 있는 코드가 실행이 된다.

#     조건에는 True, False,
#     또는 그에 준하는(T, F로 형 변환이 가능한)

if '거짓':
    print('이거 프린트 될까요?')

if '':
    print('이건요?')
    
if 0:
    print('이거ㅛ?')


# else, 조건이 False인 경우에 실행
# condition = True
condition = False
if condition:
    print('condition이 True인 경우에 실행')
else:
    print('conditino이 False인 경우에 실행')

# 학점

grade = 3.7

if grade >= 4:
    print('a')

if grade >=3 and grade < 4:
    print('b')

# if grade >= 4:
#     print('a')
# else:
#     if grade >=3 :
#         print('b')
#     else:
#         if grade >=2 :
#             print('c')
#         else:
#             if grade >= 1:
#                 print('d')
#             else:
#                 print('f')

if grade >= 4:
    print('a')
elif grade >= 3 :
    print('b')
elif grade >= 2 :
    print('c')
elif grade >= 1:
    print('d')
else:
    print('f')

# s학점 추가
if grade == 4.3:
    print('s')
elif grade >= 4:
    print('a')
elif grade >= 3 :
    print('b')

if grade >= 4:
    if grade == 4.3:
        print('s')
    else:
        print('a')
elif grade >= 3 :
    print('b')


# dust = int(33.1) # 33, 양수
dust = int(input())
# if dust >= 0 and dust <= 15:
#     print('좋음')
#
# if dust >= 16 and dust <= 35:
#     print('보통')


if dust >= 0 and dust <= 15:
    print('좋음')
elif dust <= 35:
    print('보통')
elif dust <= 75:
    print('나쁨')
else:
    print('매우 나쁨')








# 2.a
# 40 이하의 3의 배수를 출력하시오(3단의 확장). 반복의 종류는 자유롭게 사용하시오.

num = 1
while True:
    if 3 * num > 40:
        break
    print(3 * num)
    num += 1

# num = 0
# while True:
#     num += 1
#     print(3 * num)

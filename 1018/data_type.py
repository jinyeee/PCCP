num = 1 # 숫자.
num_str = '1' # 문자열

str(num) # 형변환, 문자열
int(num_str) # 형변환, 정수형
float(num_str) # 형변환, 실수형

print(num)
print(num_str)

# 주석 이라고 합니다.
# 코드의 실행에 전혀 영향을 미치지 않는 줄
# 코드의 설명 등등을 적기 위해서 사용한다.
# ctrl + / 로 쉽게 사용이 가능합니다.


# 사용자에게 입력
# input_num1 = int(input())
#
# input_num2 = input()
# input_num2 = int(input_num2)
#
# print(input_num1 + input_num2)

print(bool('1')) # True
print(bool(1)) # True
print(bool(0)) # False
print(bool(-1)) # True

print() # 줄바꿈, enter
print(bool('')) # 없는, 빈 문자열, False
print(bool(' ')) # True



# 값 swap
num1 = 1
num2 = 2

# tmp = num2
# num2 = num1
# num1 = tmp
num1, num2 = num2, num1 # 동시할당
print(num1, num2)









# def func_name(input):
#     기능을 하는 코드
#     재료인 input을 사용해서
#
#     return 결과값

def add_1(x):
    y = x + 1
    return y

# 코드의 재활용을 할 때 많이 사용.
result = add_1(3)


result = print('안녕')

print(result)

# input, output 선택이다. 필요에 의해 생략 가능
# 기능은 function의 의의이기 때문에 생략할 필요가 없다?
def func():
    pass

print(func())

# 소수를 판별하는 함수를 만들고 싶다.

n = 17
is_prime = True
for num in range(2, n):
    if n % num == 0:
        is_prime = False

print(is_prime)

n = 18
is_prime = True
for num in range(2, n):
    if n % num == 0:
        is_prime = False

print(is_prime)

n = 20
is_prime = True
for num in range(2, n):
    if n % num == 0:
        is_prime = False

print(is_prime)


n = 18
def check_prime(n):
    is_prime = True
    for num in range(2, n):
        if n % num == 0:
            is_prime = False
    return is_prime

is_prime_18 = check_prime(18)
print(is_prime_18)
print()

lst = [1, 2, 3]
result = lst.append(3)
print(result)

popped_el = lst.pop()
print(popped_el)

# 함수는 함수 바깥에 영향을 미치면 절대 안됩니다.
# 따라서, list의 append의 경우 함수가 아닌 메서드로서
# list에 변화를 일으키는 방향으로 설계가 되었습니다.

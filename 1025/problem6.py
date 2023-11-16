# 6.
# n = 17일 때, n이 소수인지 판단하시오. (추가로, n을 입력받아 같은 과정을 반복하시오.)

# n은 소수인가?

# 약수가 1, n뿐인 수가 소수다.

# 2 ~ n-1 까지의 수로 나눴을 때 나머지가 0이 아니라면
# 소수다.

# 2 ~ n-1 까지의 수로 나눴을 때 나머지가 0이 라면
# 소수가 아니다.

n = 17
is_prime = True
for num in range(2, n):
    if n % num == 0:
        is_prime = False

print(is_prime)



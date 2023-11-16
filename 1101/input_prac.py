value = input()
print(value)

value = value.split()
print(value)

# map(func, container)
# container의 원소들을 각각 func에 통과시켜서
# 결과값들은 list와 비슷한 형태로 만들어 줌

# 단, map 이라는 형태로 감싸주기 때문에, 눈으로 보기 위해서는
# list로 형변환을 다시 시켜줘야 함.

value = list(map(int, value))
print(value)

# x, y, z, r = value
# x = value[0]
# 정 모르겠다, 이걸 외우자...!
value = list(map(int,input().split()))
print(value)
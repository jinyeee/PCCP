
# x에다가 1을 더해줍니다
# 그녀석을 우리에게 보여줍니다.
def add_1_and_print(x):
    print(x+1)

# x에다가 1을 더해줍니다
# 그녀석을 우리에게 반환해줍니다.(사용할 수 있도록 해준다)
def add_2(x):
    return x+2

y = add_1_and_print(10)
z = add_2(10)
print(y, z)


# print의 경우, 개발할 때 우리가 값을 확인하기 위해서
# 또는 알고리즘 문제에서 '출력하시오' 라고 되어있을 때
# 등등... 만 사용.
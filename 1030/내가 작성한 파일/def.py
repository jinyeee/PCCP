def func_1(x):
    print(x+1)

def func_2(x):
    return x+2

# 값을 반환하려면 print가 아닌
# return으로 작성해줘야한다
# 반환 -> 사용할 수 있도록 해준다.    
# 우리에게 반환해준다 -> 그 값을 사용할 수 있음*

# print의 경우, 개발할 때 우리가 값을 확인하거나
# 알고리즘 문제에서 '출력하시오'라고 요구할때

y = func_1(10) # return값이 None
z = func_2(10)
print(y,z)





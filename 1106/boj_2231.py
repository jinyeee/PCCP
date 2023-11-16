# boj : 백준 온라인 저지를 말합니다
# 분해합

n = int(input())

# 245 + 2 + 4 + 5
# 어떤 숫자가 주어졌을 때 그것의 분해합을 구하는 기능
def div_sum(n):
    result = n
    for num in str(n):
        result += int(num)
    # print(result)
    return result

print(div_sum(245))
flag = '실패'
# is_succees

for num in range(n):
    if div_sum(num) == n:
        print(num) # 정답이야.
        flag = '성공'
        break
else:
    print(0)
if flag == '실패':
    print(0)
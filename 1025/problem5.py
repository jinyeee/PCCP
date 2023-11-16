# 5.
# 1 ~ 9 까지의 자연수 중 제곱한 수가 10 이상 50 이하인 자연수의 리스트를 출력해보세요.

# 1부터 9까지 숫자를 반복.
# 	숫자를 제곱을 합니다.
# 	숫자가 10이상 50 이하인지 확인을 합니다.
# 		맞다면 리스트에 담습니다.

lst = []
for num in range(1, 10):
    square = num ** 2
    if square >= 10 and square <= 50:
        lst.append(num)

print(lst)
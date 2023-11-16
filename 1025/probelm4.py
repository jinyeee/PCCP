# 4.
# lst = [1,2,3,4,5,6,7] 일 때,
# 원소가  1, 4, 5, 7인 경우를 제외하고 출력하세요

lst = [1,2,3,4,5,6,7]
do_not_print = [1, 4, 5, 7]
# if True:
#     실행해.
# else:

# 1
for num in lst:
    if (num == 1) or (num == 4) or (num == 5) or (num == 7):
        continue
    # 만약 1, 4, 5, 7이면
    #     실행시키지 마!
    print(num)
print()

# 2
for num in lst:
    if (num == 1) or (num == 4) or (num == 5) or (num == 7):
        # 아무것도 하지 마
        pass
    else:
        print(num)
print()

# 3
for num in lst:
    if num in do_not_print:
        continue
    print(num)
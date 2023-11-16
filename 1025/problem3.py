# 3.
# 1 ~ 100 중에 7의 배수의 개수를 출력하세요.
# psudocode
# 1부터 100까지 반복
# 	숫자를 7의 배수인지 판단하는 행동을.
# 	if 7의 배수이니?
# 		개수를 늘려줄게.

# 1. for를 사용한 직관적인 방법.
count = 0
for num in range(1, 100 + 1):
    if num % 7 == 0:# 7의 배수이면
        count += 1

print(count)

# 2. while을 사용한 7씩 늘려주는 방법.
# 7 step씩 더해줘서 위의 식보다 약 7배 빠르다.
num = 0
count = 0 # 선언, 할당(초기값)
while True:
    num += 7
    if num > 100:
        break
    count += 1
print(count)

# 3. range의 step을 활용한 방법.
count = 0
for num in range(7, 101, 7):
    count += 1
print(count)

# 4. 배수의 개수 라는 개념을 다시 생각한 방법
print(len(range(7, 101, 7)))

# 5. 배수의 개수가 뭐지?
print(100 // 7)


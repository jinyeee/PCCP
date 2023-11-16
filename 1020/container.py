# list
# 순서가 있다. (index로 접근이 가능하다 - ?)

names = ['jun', 'alex', 'ken']

# 사용
print(names[0])

# 음수의 인덱스도 가능합니다.
print(names[-1])

# 수정
name = 'jun'
# 이름을 준으로 바꿔줘 - 재할당을 통해
name = '준'

names[0] = '준'
print(names)

# 리스트의 덧셈
lst = [1, 2] + [3, 4]
print(lst)

# 리스트의 곱셈
print([1, 2] * 3)


# 슬라이싱
numbers = [1, 2, 3, 4, 5, 6, 7]

# numbers[ 범위 ]
# numbers[ 시작 인덱스 : 끝나는 인덱스 : step]
print(numbers[1:4])

# 범위에서
# 1.
# 첫번째 인덱스는 포함
# 두번째 인덱스는 불포함

# 2.
# 인덱스의 앞에 막대기를 세운다고 생각을 해봅니다.
# 그 막대기에 인덱스를 붙여주고, 해당 막대기 사이의 범위

# step?
print(numbers[1 : 5 : 2])


# 숫자를 생략하면 '전체'를 나타냅니다.

print(numbers[:6]) # 처음부터 6번째 인덱스까지
print(numbers[6:]) # 6번째부터 마지막까지

# 음수에 대한 슬라이싱도 가능.
print(numbers[::-1])

# 리스트에서 원소의 삽입
names = ['j', 'a', 'k']
name = 's'

# names = names + [name]
something = names.append(name)
print(names)
print(something)

# 리스트에서 원소의 삭제
# names = names[:-1]
popped_el = names.pop()
print(names)
print(popped_el)
# pop은 마지막 원소를 삭제합니다.
# 단, 인덱스를 명시해주면 해당 index의 원소를 삭제합니다.
names.pop(1)
print(names)


# string
# f-string - string에서 변수를 활용할 경우.
name = 'jun'
name2 = 'alex'

print(f'안녕, {name}')
print(f'안녕, {name2}')


# range
# 수열
# 슬라이싱의 사용법과 비슷.
# 시작인덱스, 끝인덱스, step
print(list(range(3, 7)))

print(list(range(8)))


# 멤버십 연산자

names = ['j', 'a', 'k']

print('s' in names) # False
print('j' in names) # True

print('s' not in names) # True






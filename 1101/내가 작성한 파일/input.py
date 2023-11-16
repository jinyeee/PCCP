value = input()
print(value)

value = value.split() # 띄어쓰기를 기준
print(value)

list = []
# 파이썬 리스트 생성
for i in value:
    list.append(int(i))

# map
# func, container
value = list(map(int, value))
value = list(map(int, input().split()))

#map에 왜 넣어줘야하는지..?



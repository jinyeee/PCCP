#
#
# # 정렬
#
# # 메서드 .sort() => 반환값이 존재하지 않음.
# # 앞에 나와있는 매개체로서의 list가 정렬이 된다.
# # 즉, 자기 자신이 정렬이 된다.
# lst = [1, 11, 5, 4, 8, 13, 20, 2]
# sorted_lst = lst.sort()
# print(lst)
# print(sorted_lst)
#
# print()
# # 함수 sorted() => 반환값이 존재합니다.
# # 즉, 원본 리스트는 보존한 채 새로운 리스트가 생성됩니다.
# lst = [1, 11, 5, 4, 8, 13, 20, 2]
# sorted_lst = sorted(lst)
# print(lst)
# print(sorted_lst)
#

# (키, 몸무게) 의 data들이 있을때,
# 1. 키 순으로 정렬
# 2. 몸무게 순으로 정렬
data = [[170, 60], [180, 40], [150, 50]]

data.sort()
print(data)

def order(el): # el : [a,b] 형태의 데이터입니다.
    return el[1]
    # return el[0] ** 2 // el[1] # 가상의 bmi

# data.sort(key=func)
data.sort(key=order)
# data.sort(key= lambda  x : x[1])
print(data)





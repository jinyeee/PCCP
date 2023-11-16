from pprint import pprint
# 모듈 : 누군가가 만든 코드덩어리
# 앞은 모듈 뒤는 func의 이름
# from pandas import DataFrame
# pandas는 모듈의 이름 dataFrame은 함수의 이름
# 필요한 값만 가져오기 위해서 -> 훨씬 더 가벼움*


# 2차원 배열 생성

# 1-9까지 반복 n단 반복
# 2-9까지 반복 : 곱해줄 값



gugudan = []
for num in range(2, 10):
    n_dan = []
    for i in range(1, 10):
        n_dan.append(num * 1)
    #print(n_dan)
    gugudan.append(n_dan)
pprint(gugudan)
#print(gugudan)


def make_n_dan(num):
    n_dan = []
    for i in range(1, 10):
        n_dan.append(num * 1)

    return n_dan



# 함수를 만들고 함수 호출해서 코드를 줄이고
# 유지보수하기 쉽도록 
gugudan = []
for num in range(2, 10):
    n_dan = make_n_dan(num)
    gugudan.append(n_dan)

def make_n_m_dan(n, m):
    gugudan = []
    for num in range(2, n+1):
        n_dan = []
        for i in range(1, m+1):
            n_dan.append(num * 1)   
        gugudan.append(n_dan)
    return gugudan

print(make_n_m_dan)


# 사다리타기
# 조건문 0 or 1 
# 추상화시키기

# 잘못된 방법
n = 5
grid = [[0] * n ]*n
pprint(grid)
grid[0][0] = 100


# 맞는 방법
grid = []
for _ in range(n):
    small_grid = [0]*n
    grid.append(small_grid)




#리스트 컴프리헨션을 사용해서 위의 반복문을 한번 더 축약 가능.
grid = [[0]*n for _ in range(n)]


pprint(grid)

# 구구단과 grid 생성하는 내용 복습

# 얕은 복사, 1차원일때만 가능
list1 = [1, 2, 3]
list2 = list1 # list1의 주소를 복사 그대로 복사한다
# list1의 값이 변하면 list2도 변한다.

#list1의 원소값만 얻고 싶으면
list2 = list1[:]

# 얕은 복사
mat1 = [[1,2],[3,4]]
mat2 = mat1
# 밸류들을 가져온다.
# 결국 향하는 방향(주소)를 복사해온다.
# 반복 -> 재귀
# 값만 가져올 수 있을 때까지  -> 

from copy import deepcopy
# 얕은 카피를 recursive하게 하면 됩니다.

# 검색해서 사용하는 방법을 익히는 것도 반드시 필요한 태도
# 블로그를 찾는게 좋지않은 방법인데 처음에는 참고하고
# 최종적으로는 공식문서로 공부하는게 좋다**


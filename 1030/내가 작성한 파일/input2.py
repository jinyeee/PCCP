## 실습

T = int(input()) # 형변환이 필요
for _ in range(T):
    input_value = input()
    input_value = input().split()
    input_value = list(map(int, input_value))
    #input_value = list(map(int, input().split()))
    print(input_value)
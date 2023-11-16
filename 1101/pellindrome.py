# s = '123421'
# # s가 어떻게 하면 회문이지?
# s = list(s)
# # s[::-1]
# if s == s[::-1]:
#     print('yes')
# else:
#     print('no')

while True:
    s = input()
    if s == '0': # 0이 아니라 '0'인 점 조심!
        break
    s = list(s)
    if s == s[::-1]:
        print('yes')
    else:
        print('no')









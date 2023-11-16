s = '123421'
# s = '12321'

is_pellindrome = True
for index in range(len(s)//2):

    # index     compare_index
    # 0       -1     -(0 + 1)
    # 1       -2     -(1 + 1)
    # 3       -3     -(2 + 1)
    compare_index = -(index + 1)
    if s[index] != s[compare_index]:
        is_pellindrome = False
        break

if is_pellindrome:
    print('yes')
else:
    print('no')

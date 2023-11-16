s = '123421'
is_pellindrome = True
start_index = 0
end_index = len(s) - 1
# end_index = -1 # 로 해도 상관 없지만, 멈추는 조건이 달라질 예정
while True:
    # s, e 비교를 할꺼야.
    # 만약 두개가 달라?
    #     펠린드롬이 아니야.
    if s[start_index] != s[end_index]:
        is_pellindrome = False
        break

    # s는 1씩 커지고, e는 1씩 작아져.
    start_index += 1
    end_index -= 1

    # s가 e보다 커지면 멈추면 될 것 같아.
    if start_index >= end_index:
        break






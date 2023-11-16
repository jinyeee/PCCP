# 입력
n, m = map(int, input().split())
mat = [list(map(int,input().split())) for _ in range(n)]

print(mat)
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
cnt = 0
# 모든 el에 대해서
for i in range(n):
    for j in range(m):
        # 1의 개수를 세겠어.
        if mat[i][j] == 1:
            # 2와 근접한 경우에.
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                # ni, nj를 방문할 수 있니?
                # 방문할 수 있는 경우 & ni, nj가 2인 경우
                if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 2:
                    cnt += 1
                    # 1 옆에 2가 중복으로 있는 경우 방지
                    break
                # 방문할 수 없는 경우 skip해. skip되지 않았으면 ni,nj가 2인 경우
                # if 0 > ni or n <= ni or 0 > nj or m <= nj:
                #     continue
                # if mat[ni][nj] == 2:
                #     cnt += 1
                #     # 1 옆에 2가 중복으로 있는 경우 방지
                #     break

print(cnt)
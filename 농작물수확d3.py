N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

mid = N // 2 # 정수 나눗셈
total = 0

for i in range(N):
    #중심(mid)과의 거리 계산
    offset = abs(mid - i)

    #수학 범위: 시작점은 offset, 끝점은 N - offset
    for j in range(offset, N - offset):
        total += arr[i][j]

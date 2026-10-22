dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
total_sum = 0

for r in range(N):
    for c in range(N):
        current_val = arr[r][c]

        #상하좌우 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]


            if 0 <= nr < N and 0 <= nc < N:
                total_sum += abs(current_val - arr[nr][nc])
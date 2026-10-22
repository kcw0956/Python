# import sys
# input = sys.stdin.readline


# T = int(input())

# for test_case in range(1, T + 1):
#     N = int(input())

#     board = [[0] * N for _ in range(N)]

#     # 오른쪽, 아래, 왼쪽, 위
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]

#     r, c = 0, 0
#     direction = 0

#     for num in range(1, N * N + 1):
#         board[r][c] = num

#         nr = r + dr[direction]
#         nc = c + dc[direction]

#         # 범위 밖이거나 이미 숫자가 있으면 방향 전환
#         if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] != 0:
#             direction = (direction + 1) % 4
#             nr = r + dr[direction]
#             nc = c + dc[direction]

#         r, c = nr, nc

#     print(f"#{test_case}")
#     for row in board:
#         print(*row)

import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    num = int(input()) 
    board = [[0] * num for _ in range(num)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    r, c = 0, 0
    direction = 0

    for d in range(num * num):
        nr = r + dr[direction]
        nc = c + dc[direction]

        if (nc < 0 or nc >= num or nr < 0 or nr > num or board[nr][nc] != 0):
            direction = (direction + 1) % 4
            nr = r + dr[direction]
            nc = c + dc[direction]

        r, c = nr, nc
    
    print(f"#{T}")
    for row in range(num):
        print(*board(row))




import sys

input = sys.stdin.readline

num = int(input())
board = [[0] * num for _ in range(num)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

r, c = 0, 0
d = 0

for i in range(1, num * num + 1):
    board[r][c] = i
    print(r, c, board[r][c])

    nr = r + dr[d]
    nc = c + dc[d]

    if nr < 0 or nr >= num or nc < 0 or nc >= num or board[nr][nc] != 0:
        d = (d + 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]

    r = nr
    c = nc

for row in board:
    print(*row)
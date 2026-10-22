
# board = [list(map(int, input().split())) for _ in range(N)]

board = [
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33]
]

N = len(board)
M = len(board[0])

for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

print(board)

